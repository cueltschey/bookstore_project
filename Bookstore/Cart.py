import sqlite3
import os

class Cart:
    def __init__(self, user_id, database_name="MainDatabase.db"):
        self.cart_items = {}
        self.user_id = user_id
        self.database_name = database_name

    def add_book(self, book_isbn, quantity):
        if book_isbn in self.cart_items:
            self.cart_items[book_isbn] += quantity
        else:
            self.cart_items[book_isbn] = quantity

    def remove_book(self, book_isbn):
        if book_isbn in self.cart_items:
            if self.cart_items[book_isbn] > 1:
                self.cart_items[book_isbn] -= 1
            else:
                del self.cart_items[book_isbn]

    def checkout(self):
        # Implement logic to create an order and return it after payment is accepted
        pass

    def view_cart(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        print("Shopping Cart:")
        print("ISBN\tQuantity")

        for isbn, qty in self.cart_items.items():
            print(f"{isbn}\t{qty}")

        connection.close()
