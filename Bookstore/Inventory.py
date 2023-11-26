import sqlite3
import os
import sys

class Inventory:
  def __init__(self, databaseName = 'Bookstore/Inventory.db', tableName = 'Inventory'):
    self.databaseName = databaseName
    self.tableName = tableName

  def viewInventory(self):
    cursor = sqlite3.connect("./" + self.databaseName)
    book_inventory = cursor.execute(f"SELECT * FROM {self.tableName}")

    print("Book Inventory:")

    headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock", "Quantity"]
    table_data = [list(book) for book in book_inventory]
    if(len(table_data) < 1):
        print("inventory empty") 
    for book in table_data:
        for j in range(len(book)):
            print(headers[j], book[j])

  def searchInventory(self):
    cursor = sqlite3.connect("./" + self.databaseName)
    ISBN = input("enter ISBN to search: ")

    res = cursor.execute(f"SELECT * FROM {self.tableName} WHERE ISBN='{ISBN}'")
    search_result = [r for r in res] 
    if len(search_result) >= 1:
        print("Book found:")
        headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock", "Quantity"]
        table_data = [list(book) for book in search_result]
        for i in table_data:
            print("Book:","\n")
            for j in range(len(i)):
                print(headers[j] + ": ", i[j])
    else:
        print(f"No book with ISBN {ISBN} found in our inventory.")


  def decreaseStock(self, ISBN):
    cursor = sqlite3.connect("./" + self.databaseName)
    res = cursor.execute(f"SELECT Stock FROM {self.tableName} WHERE ISBN='{ISBN}'")
    search_book = [r for r in res]
    if len(search_book) < 1:
        print("Invalid ISBN.")
    else:
        current_quantity = int(search_book[0][0])
        print("Current book quantity:", current_quantity)
        quantity_to_decrease = int(input("Enter the quantity to decrease: "))
        if(current_quantity - quantity_to_decrease > 0):
            cursor.execute(f"UPDATE {self.tableName} SET Stock='{current_quantity - quantity_to_decrease}' WHERE ISBN ='{ISBN}'")
            print("Stock quantity decreased successfully. The new stock is: ", current_quantity - quantity_to_decrease)
            cursor.commit()
        elif(current_quantity - quantity_to_decrease == 0):
            cursor.execute(f"DELETE FROM {self.tableName} WHERE ISBN='{ISBN}'")
            print("book removed from inventory...")
            cursor.commit()
        else:
            print("Insufficient stock.")





