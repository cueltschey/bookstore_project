import sqlite3
import os

class User:
    def __init__(self, database="Bookstore.db", table=""):
        self.databaseName = database
        self.tableName = table
        self.userID = ""
        self.loggedIn = False
        try:
            self.cnn = sqlite3.connect("./Bookstore/" + self.databaseName)
        except Exception as e:
            raise e 

    def login(self):
        email = input("email: ")
        password = input("password: ")
        userIDs = self.cnn.execute(f"SELECT userID FROM User WHERE Email='{email}' AND Password='{password}'")
        for u in userIDs:
            self.userID = u[0]
            self.loggedIn = True
            return True
        print("login failed...")
        return False
    
    def logout(self):
        self.userID = ""
        self.loggedIn = False
        return False

    def viewAccountInformation(self):
        if(self.userID == ""):
            print("please log in...")
            return False
        info = self.cnn.execute(f"SELECT * FROM User WHERE UserID='{self.userID}'")
        for i in info:
            for x in i:
                print(x)
            return True

    def createAccount(self):
        email = input("Email: ")
        password = input("Password: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        add = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        z = input("Zip: ")
        pay = input("Payment: ")
        stmt = "INSERT INTO User VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        try:
            self.cnn.execute(stmt, (email,password,first,last,add,city,state,z,pay))
            self.cnn.commit()
        except Exception as e:
            print(e)
     
    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID

