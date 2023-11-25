import sqlite3

class Cart:
    def __init__(self, table='Cart', database="Bookstore/Bookstore.db"):
        self.databaseName = database
        self.tableName = table
        self.cnn = sqlite3.connect('./' + databaseName)

    def addToCart(self, userID, ISBN):
        books = self.cnn.execute(f"SELECT Quantity FROM Inventory WHERE ISBN='{ISBN}' AND UserID='{userID}'")
        for book in books:
            q = int(book) + 1
            self.cnn.execute(f"UPDATE Inventory SET Quantity='{q}' WHERE ISBN='{ISBN} AND UserID={userID}'")
            return True
        
        self.cnn.execute(f"INSERT INTO {self.tableName} VALUES (?,?,?)",(userID, ISBN, 1))
        return False

    def removeFromCart(self, ISBN):
        q = self.cnn.execute("SELECT Quantity FROM Inventory WHERE ISBN={ISBN} AND UserID={userID}")

    def checkOut(self, userID):
        books = self.cnn.execute(f"SELECT ISBN FROM {self.tableName} WHERE UserUD={userID}")

        for book in books:
            self.cnn.execute(f"")
        
        pass
        
    def viewCart(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        print("Shopping Cart:")
        print("ISBN\tQuantity")

        for isbn, qty in self.cartItems.items():
            print(f"{isbn}\t{qty}")

        connection.close()
