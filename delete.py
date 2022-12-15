from tkinter import *

def drop_tables():
    import cx_Oracle
    dsn_tns = cx_Oracle.makedsn("oracle.scs.ryerson.ca", "1521", "orcl")
    conn = cx_Oracle.connect(user="sbalolia", password="05257621", dsn=dsn_tns)
    c = conn.cursor()
    list = ['BOOKS','VIDEOS','RENTALORDER','ORDERS','SUPPLIERITEMS','SUPPLIERS','CUSTOMER','EMPLOYEE','PAYMENTMETHOD','LIBRARYITEM','PERSON','MEMBERSHIP']
    for i in range(len(list)):
        c.execute(f'DROP TABLE {list[i]}')
    conn.commit()
    c.close()
    conn.close()


