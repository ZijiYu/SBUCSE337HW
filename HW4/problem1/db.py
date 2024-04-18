import sys
import os
import sqlite3
from contextlib import closing

from objects import Category
from objects import Movie

conn = None


def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            print("Windows")
            DB_FILE = "movies.sqlite"
        else:
            print("Linux")
            HOME = os.environ["HOME"]
            DB_FILE = "movies.sqlite"

        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
    return conn


def close():
    if conn:
        conn.close()


def make_category(row):
    return Category(row["categoryID"], row["categoryName"])


def make_movie(row):
    return Movie(row["movieID"], row["name"], row["year"], row["minutes"],
                 make_category(row))


def get_categories():
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories


def get_category(category_id):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()
        if row:
            return make_category(row)
        else:
            return None


def get_movies_by_category(category_id):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies


def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies


def add_movie(movie):
    sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                        movie.minutes))
        conn.commit()


def delete_movie(movie_id,name):
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        if c.rowcount == 0:
            print("No such ID")
        else:
            print(name + " was deleted from database. \n")


# Initialization:

def create_category_table(conn):
    sql = '''CREATE TABLE IF NOT EXISTS Category (
             categoryID INTEGER PRIMARY KEY,
             name TEXT NOT NULL
             )'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
    conn.commit()


def initialize_category_table(conn):
    categories = [
        (1, "Animation"),
        (2, "Comedy"),
        (3, "History")
    ]
    sql = ''' INSERT INTO Category (categoryID, name)
                  VALUES(?, ?) '''
    try:
        c = conn.cursor()
        c.executemany(sql, categories)
        conn.commit()
        print("Category Successfully Initialized")
    except sqlite3.Error as e:
        print(f"{e}Category Initialized Error")


def create_movie_table(conn):
    sql = '''CREATE TABLE IF NOT EXISTS Movie (
             movieID INTEGER PRIMARY KEY AUTOINCREMENT,
             categoryID INTEGER,
             name TEXT NOT NULL,
             year INTEGER,
             minutes INTEGER,
             FOREIGN KEY (categoryID) REFERENCES Category(categoryID)
             )'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
    conn.commit()


def initialize_db(conn):
    create_category_table(conn)
    initialize_category_table(conn)
    create_movie_table(conn)


# new add features
def get_movie(movie_id):
    sql = '''SELECT name FROM Movie WHERE movieID=?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        result = c.fetchone()
    if result is not None:
        return result[0]
    else:
        return None
