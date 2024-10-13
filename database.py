import mysql.connector

def DB_connection():
    con = mysql.connector.connect(host='localhost',user='root',password='root',database='bank')
    return con

def Create_tables():
    con = DB_connection()
    cur = con.cursor()
    try:

        cur.execute("""
                        CREATE TABLE IF NOT EXISTS CUSTOMER
                        (CUSTOMER_ID INT PRIMARY KEY AUTO_INCREMENT,
                         NAME VARCHAR(30) NOT NULL,
                         PHONE_NO VARCHAR(12) NOT NULL UNIQUE, 
                         EMAIL VARCHAR(30) NOT NULL UNIQUE, 
                         PASSWD VARCHAR(100) NOT NULL
                         )""")


        cur.execute("""
                    CREATE TABLE IF NOT EXISTS ACCOUNT (
                        ACCOUNT_ID INT PRIMARY KEY AUTO_INCREMENT,
                        CUSTOMER_ID INT NOT NULL,
                        TOTAL FLOAT NOT NULL,
                        FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID)
                    )
                    """)

        cur.execute("""
                    CREATE TABLE IF NOT EXISTS TRANSCATION(
                    TRANSCATION_ID INT PRIMARY KEY AUTO_INCREMENT,
                    ACCOUNT_ID INT NOT NULL,
                    TYPE VARCHAR(10) NOT NULL,
                    AMOUNT FLOAT NOT NULL,
                    FOREIGN KEY (ACCOUNT_ID) REFERENCES ACCOUNT(ACCOUNT_ID)
                    )
                    """)
        # Commit the changes
        con.commit()

    except mysql.connector.Error as err:
        print(f"SQL ERROR: {err}")

    finally:
        cur.close()
        con.close()


Create_tables()
