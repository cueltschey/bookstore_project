import sqlite3

class Cart:
    def __init__(self, database="Bookstore/Cart.db", table='Cart'):
        self.databaseName = database
        self.tableName = table

    def addToCart(self, userID, ISBN):
        cnn = sqlite3.connect('./' + self.databaseName)
        books = cnn.execute(f"SELECT Quantity FROM Inventory WHERE ISBN='{ISBN}' AND UserID='{userID}'")
        for book in books:
            q = int(book[0]) + 1
            cnn.execute(f"UPDATE Inventory SET Quantity='{q}' WHERE ISBN='{ISBN} AND UserID={userID}'")
            return True
        
        cnn.execute(f"INSERT INTO {self.tableName} VALUES (?,?,?)",(userID, ISBN, 1))
        return False

    def removeFromCart(self, userID, ISBN):
        cnn = sqlite3.connect('./' + self.databaseName)
        cnn.execute("DELETE FROM {self.tableName} WHERE UserID='{userID}' AND ISBN='{ISBN}'")

    def checkOut(self, userID):
        cnn = sqlite3.connect('./' + self.databaseName)
        books = cnn.execute(f"SELECT ISBN, Quantity FROM {self.tableName} WHERE UserID='{userID}'")

        for book in books:
            inventory.decreaseStock(book[0], book[1])
    
        cnn.execute(f"DELETE FROM {self.tableName} WHERE UserID='{userID}'")
        cnn.commit()
        
        
    def viewCart(self, userID, inventoryDatabase="Bookstore/Inventory.db"):
        cursor = sqlite3.connect("./" + self.databaseName)
        inv = sqlite3.connect("./" + inventoryDatabase)

        res = cursor.execute(f"SELECT ISBN, Quantity FROM {self.tableName} WHERE UserID='{userID}'")
        columns = ["ISBN", "Title","Author","Genre","Pages","Date", "Quantity"]
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(columns[0],columns[1],columns[2],columns[3],columns[4],columns[5],columns[6]))
        print()

        for info in res:
            i = [item for item in inv.execute(f"SELECT * FROM Inventory WHERE ISBN='{info[0]}'")]
            i = i[0]
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(info[0],i[1],i[2],i[3],i[4],i[5],info[1]))


        cursor.close()
        inv.close()
        print()
