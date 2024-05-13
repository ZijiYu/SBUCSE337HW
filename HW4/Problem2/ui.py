#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import locale

#from business import Investment

class Investment():
    def __init__(self):
        self.monthlyInvestment = 0
        self.yearlyInterestRate = 0
        self.years = 0

    def calculateFutureValue(self):
        monthlyInterestRate = self.yearlyInterestRate / 12 / 100
        months = self.years * 12
        futureValue = 0
        for i in range(months):
            futureValue += self.monthlyInvestment
            monthlyInterestAmount = futureValue * monthlyInterestRate
            futureValue += monthlyInterestAmount
        return futureValue


class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.investment = Investment()
        result = locale.setlocale(locale.LC_ALL, '')
        # if result == 'C':
        locale.setlocale(locale.LC_ALL, 'en_US')


        # Define string variables for text entry fields
        self.monthlyInvestment = tk.StringVar()
        self.yearlyInterestRate = tk.StringVar()
        self.years = tk.StringVar()
        self.futureValue = tk.StringVar()

        self.monthlyInvestment1 = tk.StringVar()
        self.yearlyInterestRate1 = tk.StringVar()
        self.years1 = tk.StringVar()
        self.futureValue1 = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        self.pack()

        # Display the grid of labels and text entry fields
        # monthly investment
        ttk.Label(self, text="Monthly Investment:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(
            column=1, row=0)
        ttk.Label(self, text="Monthly Investment:").grid(
            column=2, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment1).grid(
            column=3, row=0)

        # yearly Interest Rate
        ttk.Label(self, text="Yearly Interest Rate:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.yearlyInterestRate).grid(
            column=1, row=1)
        ttk.Label(self, text="Yearly Interest Rate:").grid(
            column=2, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.yearlyInterestRate1).grid(
            column=3, row=1)

        # years
        ttk.Label(self, text="Years:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
            column=1, row=2)
        ttk.Label(self, text="Years:").grid(
            column=2, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years1).grid(
            column=3, row=2)

        # future value
        ttk.Label(self, text="Future Value:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.futureValue,
                  state="readonly").grid(
            column=1, row=3)
        ttk.Label(self, text="Future Value:").grid(
            column=2, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.futureValue1,
                  state="readonly").grid(
            column=3, row=3)

        self.makeButtons1()
        self.makeButtons2()
        self.makeButtons3()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons1(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=1, row=0, padx=5)
        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=0, row=0)
    def makeButtons2(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=3, row=4, columnspan=4, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate1) \
            .grid(column=1, row=0, padx=5)
        ttk.Button(buttonFrame, text="Clear", command=self.clear1) \
            .grid(column=0, row=0)

    def makeButtons3(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=5, columnspan=6, sticky=tk.E)

        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy) \
            .grid(column=1, row=0)

    def calculate(self):
        self.investment.monthlyInvestment = float(
            self.monthlyInvestment.get())
        self.investment.yearlyInterestRate = float(
            self.yearlyInterestRate.get())
        self.investment.years = int(
            self.years.get())

        self.futureValue.set(locale.currency(
                self.investment.calculateFutureValue(), grouping=True))
    def calculate1(self):
        self.investment.monthlyInvestment = float(
            self.monthlyInvestment1.get())
        self.investment.yearlyInterestRate = float(
            self.yearlyInterestRate1.get())
        self.investment.years= int(
            self.years1.get())

        self.futureValue1.set(locale.currency(
                self.investment.calculateFutureValue(), grouping=True))

    def clear(self):
        self.monthlyInvestment.set('')
        self.yearlyInterestRate.set('')
        self.years.set('')
        self.futureValue.set('')

        self.investment.monthlyInvestment = 0.0
        self.investment.yearlyInterestRate = 0.0
        self.investment.years = 0
    def clear1(self):
        self.monthlyInvestment1.set('')
        self.yearlyInterestRate1.set('')
        self.years1.set('')
        self.futureValue1.set('')

        self.investment.monthlyInvestment1 = 0.0
        self.investment.yearlyInterestRate1 = 0.0
        self.investment.years1 = 0


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    FutureValueFrame(root)
    root.mainloop()
