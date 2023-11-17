import sqlite3
import os
import sys
os.system("python3 Bookstore/Inventory.py")

class Inventory:
  def __init__(self, databaseName = '', tableName = ''):
    self.databaseName = databaseName
    self.tableName = tableName

  def viewInventory(self):
    cursor.execute("SELECT * FROM Inventory")
    book_inventory = cursor.fetchall()

    print("Book Inventory:")

    headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock", "Quantity"]
    table_data = [list(book) for book in book_inventory]

    table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
    print(table)

    cursor.close()
    connection.close()

def searchInventory(self):
  from tabulate import tabulate
  cursor = connection.cursor()
  
  data = input("Enter the book's ISBN: ")

  query = "SELECT * FROM Inventory WHERE ISBN = ?"
  cursor.execute(query, (data,))
  search_result = cursor.fetchall()
  
  if search_result:
    print("Book found:")
    headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock", "Quantity"]
    table_data = [list(book) for book in search_result]
    table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
    print(table)
  else:
    print(f"No book with ISBN {data} found in our inventory.")
    
  cursor.close()
  connection.close()



