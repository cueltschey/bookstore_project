import sqlite3
import os

class User:
    def __init__(self, database="Bookstore/User.db", table="User"):
        self.databaseName = database
        self.tableName = table
        self.userID = ""
        self.loggedIn = False

    def login(self):
        cnn = sqlite3.connect('./' + self.databaseName)
        email = input("email: ")
        password = input("password: ")
        userIDs = cnn.execute(f"SELECT userID FROM {self.tableName} WHERE Email='{email}' AND Password='{password}'")
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
        cnn = sqlite3.connect('./' + self.databaseName)
        if(self.userID == ""):
            print("please log in...")
            return False
        info = cnn.execute(f"SELECT * FROM {self.tableName} WHERE UserID='{self.userID}'")
        for i in info:
            for x in i:
                print(x)
            return True

    def createAccount(self):
        cnn = sqlite3.connect('./' + self.databaseName)
        email = input("Email: ")
        password = input("Password: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        add = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        z = input("Zip: ")
        pay = input("Payment: ")
        stmt = f"INSERT INTO {self.tableName} VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        try:
            cnn.execute(stmt, (email,password,first,last,add,city,state,z,pay))
            cnn.commit()
        except Exception as e:
            print(e)
     
    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID

