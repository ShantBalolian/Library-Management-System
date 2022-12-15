from tkinter import *



def populate_tables():
    import cx_Oracle
    dsn_tns = cx_Oracle.makedsn("oracle.scs.ryerson.ca", "1521", "orcl")
    conn = cx_Oracle.connect(user="sbalolia", password="05257621", dsn=dsn_tns)
    c = conn.cursor()


    pop_person = """
        INSERT ALL
        INTO person
        VALUES('1987/02/01','sean12@gmail.com',647123456, 'pass123', 'sean','beasley','Ontario','Toronto','Canada','214 Jane St.')
        INTO person
        VALUES('1987/02/01','nat10@gmail.com',647654321, 'asdsad','nat','James','Ontario','Toronto','Canada','2134 Kennedy E.')
        INTO person
        VALUES('1987/02/01','BobP@gmail.com',647654321, 'notapassword','Bob','Pierce','Ontario','Toronto','Canada','412 Lawrence Ave. E.')
        INTO person
        VALUES('1987/02/01','RobH@gmail.com',647654321, 'iloveyou','Rob','Harden','Ontario','Toronto','Canada','230 Eglinton Ave. W.')
        INTO person
        VALUES('1987/02/01','TomA@gmail.com',647654321,'justkidding','Tom','Antetokoumpo','Ontario','Toronto','Canada', '100 Finch Ave. E.')
        SELECT 1 FROM DUAL
    """

    c.execute(pop_person)
    conn.commit()




    c.execute(''' INSERT ALL
    INTO Membership VALUES (1,10,'1987/02/01','SILVER')
    INTO Membership VALUES (2,8,'1987/02/01','GOLD')
    SELECT 1 FROM DUAL  ''')
    conn.commit()


    c.execute('''
    INSERT ALL
    INTO PaymentMethod VALUES  (1,'Visa')
    INTO PaymentMethod VALUES  (2,'Debit')
    SELECT 1 FROM DUAL ''')
    conn.commit()




    c.execute('''   INSERT ALL
    INTO Customer VALUES (1,'RobH@gmail.com',1,1)
    INTO Customer VALUES (2,'TomA@gmail.com',2,2)
    SELECT 1 FROM DUAL''')
    conn.commit()




    c.execute('''
    INSERT ALL
    INTO LIBRARYITEM VALUES(1,'Romance',1,'1980/02/10',8)
    INTO LIBRARYITEM VALUES(2,'Romance',1,'1990/10/10',10)
    INTO LIBRARYITEM VALUES(3,'Action',1,'2000/11/12',10)
    INTO LIBRARYITEM VALUES(4,'Action',1,'2010/03/10',10)
    INTO LIBRARYITEM VALUES(5, 'Action', 1, '1990/04/12', 10)
    SELECT 1 FROM DUAL  ''')
    conn.commit()




    c.execute('''  INSERT ALL
    INTO BOOKS VALUES(121032992, 'MyLifeIsFun', 'John Cabuguason',1)
    INTO BOOKS VALUES(532521525, 'How To Be Smart', 'Joe Fresh',2)
    INTO BOOKS VALUES(123241412, 'I Love ME', 'Shant', 5)
    SELECT 1 FROM DUAL ''')
    conn.commit()




    c.execute('''  INSERT ALL
    INTO Videos VALUES (1,3, 'How You', 'MeStudio','John','Jason')
    INTO Videos VALUES (2,4, 'Chocolate', 'Lmao','Shant','Jason')
    SELECT 1 FROM DUAL
    ''')
    conn.commit()



    c.execute('''  INSERT ALL
    INTO RentalOrder VALUES (1,1,1,50,15,'1987/02/01','1987/02/01')
    INTO RentalOrder VALUES (2,2,2,30,5,'1987/02/01','1987/02/01')
    SELECT 1 FROM DUAL ''')
    conn.commit()





    c.execute('''  INSERT ALL
    INTO SUPPLIERS    VALUES(0,'AMD Books')
    INTO SUPPLIERS    VALUES(1,'NVIDIA Education')
    SELECT 1 FROM DUAL
    ''')
    conn.commit()



    c.execute(''' INSERT ALL
    INTO SUPPLIERITEMS VALUES(1,0,'How to read for dummies','Book')
    INTO SUPPLIERITEMS VALUES(2,1,'MYSQL 101','Book')
    SELECT 1 FROM DUAL  ''')
    conn.commit()




    c.execute('''
    INSERT ALL
    INTO ORDERS VALUES(1,1,1,7,2,'2020/10/15')
    INTO ORDERS VALUES(2,0,1,15,3,'2020/11/02')
    INTO ORDERS VALUES(3,1,2,25,3,'2019/05/25')
    INTO ORDERS VALUES (4,0,1,5,23,'2019/02/05')
    SELECT 1 FROM DUAL ''')
    conn.commit()


    c.execute('''  INSERT ALL
    INTO EMPLOYEE VALUES(1,1,'sean12@gmail.com')
    INTO EMPLOYEE VALUES(2,1,'nat10@gmail.com')
    INTO EMPLOYEE VALUES(3,1,'BobP@gmail.com')
    SELECT 1 FROM DUAL
                    ''')
    conn.commit()
    c.close()
    conn.close()
