import sqlite3
import os

class Cart:
    def __init__(self, userID, database="Bookstore.db"):
        self.cartItems = {}
        self.userID = userID
        self.database = database

    def addBook(self, ISBN, quantity):
        if ISBN in self.cartItems:
            self.cartItems[ISBN] += quantity
        else:
            self.cartItems[ISBN] = quantity

    def removeBook(self, ISBN):
        if ISBN in self.cartItems:
            if self.cartItems[ISBN] > 1:
                self.cartItems[ISBN] -= 1
            else:
                del self.cartItems[ISBN]

    def checkOut(self):
        pass

    def viewCart(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        print("Shopping Cart:")
        print("ISBN\tQuantity")

        for isbn, qty in self.cartItems.items():
            print(f"{isbn}\t{qty}")

        connection.close()
