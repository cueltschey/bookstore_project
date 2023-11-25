import sqlite3
import os
import sys
os.system("python3 Bookstore/Inventory.py")
from tabulate import tabulate

class Inventory:
  def __init__(self, databaseName = 'Bookstore/Bookstore.db', tableName = ''):
    self.databaseName = databaseName
    self.tableName = tableName
    self.cursor = sqlite3.connect("./" + databaseName)

  def viewInventory(self):
    self.cursor.execute("SELECT * FROM Inventory")
    book_inventory = cursor.fetchall()

    print("Book Inventory:")

    headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock", "Quantity"]
    table_data = [list(book) for book in book_inventory]

    table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
    print(table)

def searchInventory(self):
  
  data = input("Enter the book's ISBN: ")

  cursor.execute(f"SELECT * FROM Inventory WHERE ISBN='{data}'")
  search_result = cursor.fetchall()
  
  if search_result:
    print("Book found:")
    headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock", "Quantity"]
    table_data = [list(book) for book in search_result]
    table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
    print(table)
  else:
    print(f"No book with ISBN {data} found in our inventory.")


def decrease_stock(self):

  ISBN = input("Enter the unique ISBN of the book: ")
  query = 
  cursor.execute(f"SELECT ISBN, Quantity FROM Inventory WHERE ISBN = {ISBN}")
  search_book = cursor.fetchone()
  if not search_book:
    print("Invalid ISBN.")
  else:
    current_quantity = int(search_book[1])
    print("Current book quantity:", current_quantity)
    quantity_to_decrease = int(input("Enter the quantity to decrease: "))
    if current_quantity >= quantity_to_decrease:
      new_quantity = current_quantity - quantity_to_decrease
      cursor.execute(f"UPDATE Inventory SET Quantity ='{new_quantity}' WHERE ISBN ='{ISBN}'")
      print("Stock quantity decreased successfully. The new stock is: ", new_quantity)
      connection.commit()
    else:
      print("Insufficient stock.")

def checkOut(self):

  # figure out the checkOut function





