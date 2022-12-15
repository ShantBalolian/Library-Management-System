from tkinter import *

def create_tables():
    import cx_Oracle
    dsn_tns = cx_Oracle.makedsn("oracle.scs.ryerson.ca", "1521", "orcl")
    conn = cx_Oracle.connect(user="sbalolia", password="05257621", dsn=dsn_tns)
    c = conn.cursor()


    create_table = """
        CREATE TABLE Person (
            BirthDate DATE,
            Email VARCHAR2(20) NULL,
            Phone VARCHAR2(25),
            Pass VARCHAR(20),
            FirstName VARCHAR2(20) NULL,
            LastName VARCHAR2(20) NULL,
            Province VARCHAR2(20),
            City VARCHAR2(20),
            Country VARCHAR2(20),
            StreetName VARCHAR2(20),
            PRIMARY KEY (email)
        )
    """
    c.execute(create_table)
    c.execute(''' CREATE TABLE Membership (
    MembershipId INT,
    NumOfBooksAllowed INT NOT NULL,
    MembershipExpiration DATE,
    MembershipName VARCHAR2(10),
    PRIMARY KEY (MembershipId)
                )
                ''')

    c.execute(''' CREATE TABLE PaymentMethod(
    PaymentMethodId INT PRIMARY KEY,
    PaymentType VARCHAR(10)
            )''')
    c.execute('''CREATE TABLE Customer(
    CustomerId INT PRIMARY KEY,
    Email VARCHAR(20),
    PaymentMethodId INT,
    MembershipId Int,
    FOREIGN KEY(Email) REFERENCES Person(Email) ON DELETE CASCADE,
    FOREIGN KEY(PaymentMethodId) REFERENCES PaymentMethod(PaymentMethodId) ON DELETE CASCADE,
    FOREIGN KEY(MembershipId) REFERENCES Membership(MembershipId) ON DELETE CASCADE
            ) ''')


    library_item = """
        CREATE TABLE LibraryItem (
            ItemId INT,
            Genre VARCHAR(20),
            AvailabilityStatus INT NOT NULL,
            DatePublished DATE NOT NULL,
            Rating INT,
            PRIMARY KEY(ItemId)
        )
    """

    c.execute(library_item)


    books = """
        CREATE TABLE Books (
            ISBN INT PRIMARY KEY,
            Title VARCHAR(20),
            Author VARCHAR(20) NOT NULL,
            LibraryItemNumber INT NOT NULL,
            FOREIGN KEY(LibraryItemNumber) REFERENCES LibraryItem(ItemId) ON DELETE CASCADE
        )
    """
    c.execute(books)

    videos = """
        CREATE TABLE Videos (
            VideoId INT PRIMARY KEY,
            LibraryItemNumber INT NOT NULL,
            Title VARCHAR(20),
            ProductionStudio VARCHAR(20) NOT NULL,
            KeyCast VARCHAR(20),
            Director VARCHAR(20) NOT NULL,
            FOREIGN KEY(LibraryItemNumber) REFERENCES LibraryItem(ItemId) ON DELETE CASCADE
        )
    """
    c.execute(videos)

    c.execute('''CREATE TABLE RentalOrder(
    LibraryItemId INT,
    PaymentMethodId INT,
    CustomerId INT,
    Quantity INT not NULL,
    OverdueAmount INT,
    ReturnDate DATE,
    RentalDate DATE,
    FOREIGN KEY(LibraryItemId) REFERENCES LibraryItem(ItemId) ON DELETE CASCADE,
    FOREIGN KEY(PaymentMethodId) REFERENCES PaymentMethod(PaymentMethodId) ON DELETE CASCADE,
    FOREIGN KEY(CustomerId) REFERENCES Customer(CustomerId) ON DELETE CASCADE
            ) ''')
    c.execute('''CREATE TABLE Suppliers(
    SupplierId INT NOT NULL PRIMARY KEY,
    SupplierName VARCHAR(40) NOT NULL
            )
            ''')
    c.execute('''CREATE TABLE  SupplierItems(
    SupplierItemId INT NOT NULL PRIMARY KEY,
    SupplierId INT NOT NULL,
    ItemName VARCHAR(40),
    ItemType VARCHAR(40),
    FOREIGN KEY(SupplierId) REFERENCES Suppliers(SupplierId) ON DELETE SET NULL
            ) ''')
    c.execute('''CREATE TABLE Orders(
    OrderId INT NOT NULL PRIMARY KEY,
    SupplierId INT NOT NULL,
    SupplierItemId INT NOT NULL,
    OrderStatus INT NOT NULL,
    Quantity INT NOT NULL,
    OrderDate DATE,
    FOREIGN KEY(SupplierId) REFERENCES Suppliers(SupplierId) ON DELETE SET NULL,
    FOREIGN KEY(SupplierItemId) REFERENCES SupplierItems(SupplierItemId) ON DELETE SET NULL
            )
            ''')
    c.execute(''' CREATE TABLE Employee(
    EmployeeId INT NOT NULL PRIMARY KEY,
    ManagerId VARCHAR(40),
    Email VARCHAR(20) not NULL,
    FOREIGN KEY(email) REFERENCES Person(email) ON DELETE SET NULL
            )''')


    c.close()
    conn.close()
