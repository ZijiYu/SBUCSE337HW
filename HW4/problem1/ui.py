#!/usr/bin/env/python3

import db
from objects import Movie

def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("min  - View movies by minutes")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print("------")
def display_categories():
    print()
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print("------")

def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_category():
    display_categories()
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
def display_movie_by_minutes():
    minu = int(input("Maximum number of minutes: "))
    print()
    movies = db.get_movie_by_minutes(minu)
    display_movies(movies,str(minu))
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def year_check(year):
    if year<1895:
        print("Tips: Movie was be invented since 1895")
        year=int(input("Year: "))
        return year_check(year)
    elif year>2024:
        print("Error: Invalid Year")
        year = int(input("Year: "))
        return year_check(year)
    else:
        return year
def add_movie():
    name        = input("Name: ")
    year        = year_check(int(input("Year: ")))
    minutes     = int(input("Minutes: "))
    display_categories()
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:        
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(f"'{name}' was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    # get name of the movie
    name=db.get_movie(movie_id)
    confirm = input(f"Delete '{name}' ? (y/n):")
    if confirm.lower() == 'y':
        db.delete_movie(movie_id,name)
        #print("Movie ID " + str(movie_id) + " was deleted from database.\n")

        
def main():
    conn=db.connect()
    db.initialize_db(conn)
    display_title()
    display_categories()
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "min":
            display_movie_by_minutes()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
