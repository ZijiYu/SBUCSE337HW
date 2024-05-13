#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        # Define string variables for text entry fields
        self.miles = tk.StringVar()
        self.gallon_of_gas = tk.StringVar()
        self.mpg = tk.StringVar()

        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.miles).grid(
            column=1, row=0)

        ttk.Label(self, text="Gallon of Gas Used:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gallon_of_gas).grid(
            column=1, row=1)
        ttk.Label(self, text="Miles pre Gallon:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.mpg,state="readonly").grid(
            column=1, row=2)

        self.make_button()

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
    def make_button(self):
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=1, row=0, padx=5)
    def calculate(self):
        temp=float(self.miles.get())/float(self.gallon_of_gas.get())
        self.mpg.set(format(temp,".2f"))
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Program Title")
    MyFrame(root)
    root.mainloop()
