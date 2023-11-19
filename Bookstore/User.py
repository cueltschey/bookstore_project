import sqlite3
import os
os.system("python3 Bookstore/Inventory.py")

class User:
    def __init__(self, database="Bookstore.db", table=""):
        self.databaseName = database
        self.tableName = table
        self.userID = ""
        self.loggedIn = False
        try:
            self.cnn = sqlite3.connect("./" + self.databaseName)
        except Exception as e:
            raise e 

    def login(self):
        email = input("email: ")
        password = input("password: ")
        userIDs = self.cnn.execute(f"SELECT userID FROM User WHERE Email='{email}' AND Password='{password}'")
        for u in userIDs:
            self.userID = u[0]
            return True
        print("login failed...")
        return False

    def viewAccountInformation():
        if(!userID):
            print("please log in...")
            return False
        info = self.cnn.execute(f"SELECT * FROM User WHERE UserID='{userID}'")
        for i in info:
            for x in i:
                print(i)
            return True
        

    def viewCart(self, userID, inventoryDatabase):
        # get and display books in the users cart
        items = self.cnn.execute("SELECT * FROM Cart")
        for item in items:
            print(item)
        

    def addToCart(userID, ISBN):
        # add a new book or increment existing book
        quantity = self.cnn.execute(f"SELECT Quantity FROM Cart WHERE ISBN='{ISBN}' AND UserID='{userID}'")
        self.cnn.execute(f"REMOVE FROM Cart WHERE ISBN='{ISBN}' AND UserID='{userID}'")
        if(quantity):
            quantity = int(quantity)
            self.cnn.execute("INSERT INTO Cart VALUES (?, ?, ?)", (userID, ISBN, quantity + 1))
        else:
            self.cnn.execute("INSERT INTO Cart VALUES (?, ?, ?)", (userID, ISBN, 1))

    def removeFromCart(userID, ISBN):
        # remove all books of matching ISBN
        self.cnn.execute(f"REMOVE FROM Cart WHERE UserID='{userID}' AND ISBN='{ISBN}'")

    def checkOut(userID):
        # clear cart and call inventory checkout
        items = cnn.execute(f"SELECT * FROM Cart WHERE userID='{userID}'")
        self.cnn.execute(f"REMOVE FROM Cart WHERE userID='{userID}'")


