login_check = """

    SELECT EMAIL, PASS
    FROM PERSON
    WHERE EMAIL = '{}' and PASS = '{}'
"""


create_account = """
    INSERT INTO PERSON
    VALUES('1987/02/12','atomtest@gmail.com','6471123456', 'pas4s123', 's5ean','beasl1ey','Onta1rio','Toro1nto','Canada','214 Jane St.')
"""
