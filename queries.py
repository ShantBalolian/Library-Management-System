import cx_Oracle
dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
c = conn.cursor() 
def query1():
	dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
	conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
	c = conn.cursor()
	c.execute("""SELECT c.CUSTOMERID, c.EMAIL, m.MEMBERSHIPNAME
	FROM CUSTOMER c
	JOIN MEMBERSHIP m
	ON c.MEMBERSHIPID = m.MEMBERSHIPID  """)
	conn.commit()
	records = c.fetchall()
	for rows in records:
		print (rows)
	c.close()
	conn.close()

def query2():
	dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
	conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
	c = conn.cursor() 
	c.execute('''SELECT 
			    ORDERID,
			    ORDERDATE,
			    'ACTIVE' AS status
			FROM ORDERS 
			WHERE ORDERDATE >= '2020/02/02'
			UNION
			SELECT 
			    ORDERID,
			    ORDERDATE,
			    'ARCHIVED' AS status
			FROM ORDERS 
			WHERE ORDERDATE < '2020/02/02' ''')
	conn.commit()
	c.close()
	conn.close()
def query3():
    passdsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''SELECT 
	e.EMPLOYEEID,
	p.EMAIL,
	p.PHONE,
	m.EMAIL AS MANAGER
	FROM EMPLOYEE e
	JOIN EMPLOYEE m
	ON e.EMPLOYEEID = m.MANAGERID
	JOIN PERSON p
	ON e.EMAIL = p.EMAIL ''')
    conn.commit()
    c.close()
    conn.close()
	
def query4():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''SELECT
				L.ITEMID,
				L. GENRE,
				L.AVAILABILITYSTATUS,
				L.RATING,
				V.PRODUCTIONSTUDIO,
				v.DIRECTOR
			FROM LIBRARYITEM L
			JOIN VIDEOS V
				ON V.LIBRARYITEMNUMBER = L.ITEMID ''')
    conn.commit()
    c.close()
    conn.close()

def query5():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''SELECT *
			FROM LIBRARYITEM
			WHERE GENRE  = 'Romance' ''')
    conn.commit()
    c.close()
    conn.close()

def query6():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''SELECT 
				e.EMPLOYEEID,
				e.EMAIL
			FROM EMPLOYEE e
			WHERE EMPLOYEEID < 3 ''')
    conn.commit()
    c.close()
    conn.close()

def query7():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''SELECT *
			FROM LIBRARYITEM
			WHERE availabilityStatus = 1  ''')
    conn.commit()
    c.close()
    conn.close()

def query8():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute(''' SELECT * 
			FROM PAYMENTMETHOD''')
    records = c.fetchall()
    for rows in records:
        print(rows)

    conn.commit()
    c.close()
    conn.close()

def query9():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''SELECT *
			FROM CUSTOMER c
			WHERE EXISTS 
				(SELECT NUMOFBOOKSALLOWED
				FROM MEMBERSHIP m
				WHERE c.MEMBERSHIPID = m.MEMBERSHIPID 
			AND m.MEMBERSHIPNAME = 'GOLD') ''')
    conn.commit()
    c.close()
    conn.close()

def query10():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''SELECT r.RENTALDATE, c.EMAIL, r.OVERDUEAMOUNT
			FROM RENTALORDER r, CUSTOMER c 
			WHERE c.CUSTOMERID = r.CUSTOMERID
			AND r.OVERDUEAMOUNT > 5
			ORDER BY OVERDUEAMOUNT ASC ''')
    conn.commit()
    c.close()
    conn.close()

def create_views():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''CREATE VIEW manager_phone AS
			(SELECT 
				e.EMPLOYEEID, e.EMAIL
			FROM EMPLOYEE e
			WHERE EXISTS
				(SELECT e.EMAIL
				FROM EMPLOYEE m, Person p
				WHERE e.EMPLOYEEID = m.MANAGERID
				AND e.EMAIL = p.EMAIL))


			CREATE VIEW item_order_status AS
			(SELECT 
				ORDERID,
				ORDERDATE,
				'ACTIVE' AS status
			FROM ORDERS 
			WHERE ORDERDATE >= '2020/02/02'
			UNION
			SELECT 
				ORDERID,
				ORDERDATE,
				'ARCHIVED' AS status
			FROM ORDERS 
			WHERE ORDERDATE < '2020/02/02')


			CREATE VIEW potential_employee AS
			(SELECT p.LASTNAME, p.FIRSTNAME, p.phone, p.email
			FROM PERSON p
			WHERE NOT EXISTS
				(SELECT *
				FROM EMPLOYEE e
				WHERE p.EMAIL = e.EMAIL))  ''')
    conn.commit()
    c.close()
    conn.close()

def drop_views():
    dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca','1521','orcl')
    conn = cx_Oracle.connect(user='sbalolia',password='05257621',dsn=dsn_tns)
    c = conn.cursor() 
    c.execute('''DROP VIEW item_order_status
			DROP VIEW potential_employee
			DROP VIEW manager_phone  ''')
    conn.commit()
    c.close()
    conn.close()
