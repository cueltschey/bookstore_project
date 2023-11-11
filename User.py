import sqlite3

class User:
    def __init__(self):
        self.databaseName = ""
        self.tableName = ""
    def __init__(self, databse, table):
        self.databaseName = database
        self.tableName = table

    def viewCart(self, userID, inventoryDatabase):
        # get and display books in the users cart

    def addToCart(userID, ISBN):
        # add a new book or increment existing book

    def removeFromCart(userID, ISBN):
        # remove all books of matching ISBN

    def checkOut(userID):
        # clear cart and call inventory checkout

