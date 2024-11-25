import sqlite3

conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Customers")
cursor.execute("DROP TABLE IF EXISTS Products")
cursor.execute("DROP TABLE IF EXISTS Orders")
cursor.execute("DROP TABLE IF EXISTS OrderDetails")

cursor.execute("""
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Phone TEXT,
    Address TEXT
)
""")

cursor.execute("""
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Category TEXT NOT NULL,
    Price REAL NOT NULL,
    Stock INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    OrderDate TEXT NOT NULL,
    Price REAL NOT NULL,
    TotalAmount REAL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
""")

cursor.execute("""
CREATE TABLE OrderDetails (
    OrderDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER NOT NULL,
    Price REAL NOT NULL,
    TotalAmount REAL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
)
""")

customers = [
    ("John Doe", "johndoe@example.com", "123-456-7890", "123 Elm St, Springfield"),
    ("Jane Smith", "janesmith@example.com", "234-567-8901", "456 Oak St, Springfield"),
    ("Alice Johnson", "alicej@example.com", "345-678-9012", "789 Pine St, Springfield")
]
cursor.executemany("""
INSERT INTO Customers (Name, Email, Phone, Address) VALUES (?, ?, ?, ?)
""", customers)

products = [
    ("Apple", "Fruits", 0.5, 100),
    ("Banana", "Fruits", 0.2, 150),
    ("Milk", "Dairy", 1.5, 50),
    ("Bread", "Bakery", 2.0, 30),
    ("Eggs", "Dairy", 3.0, 20)
]
cursor.executemany("""
INSERT INTO Products (Name, Category, Price, Stock) VALUES (?, ?, ?, ?)
""", products)

orders = [
    (1, "2024-11-18", 5.0)
    (2, "2024-11-18", 7.0)
    (3, "2024-11-19", 6.0)
]
cursor.executemany("""
INSERT INTO Orders (CustomerID, OrderDate, TotalAmoun) VALUES (?, ?, ?)
""", orders)