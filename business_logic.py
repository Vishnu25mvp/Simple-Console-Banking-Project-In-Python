from database import DB_connection
import hashlib
import mysql.connector


def passwd_enc(passwd: str):
    passwd = (passwd + "HEXPOP").encode('utf-8')
    passwd = hashlib.sha224(passwd).hexdigest()
    return passwd

def singin(name,ph,email,passwd):
    global con, cur
    try:
        passwd = passwd_enc(passwd)
        con = DB_connection()
        cur = con.cursor()
        cur.execute("""
                    INSERT INTO CUSTOMER (NAME,PHONE_NO,EMAIL,PASSWD)
                    VALUES (%s,%s,%s,%s)
                    """,(name,ph,email,passwd))
        print("Account Created Sucessfully")
    except mysql.connector.Error as err:
        print(f"SQL ERROR {err}")

    finally:
        con.commit()
        cur.close()


def login(email,passwd):
    global conn, account_id
    try:
        passwd = passwd_enc(passwd)
        conn = DB_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT CUSTOMER_ID
                    FROM CUSTOMER
                    WHERE EMAIL = %s AND 
                    PASSWD = %s
                    """,(email,passwd))
        account_id = cur.fetchall()[0][0]
        cur.execute("""
                    INSERT INTO ACCOUNT(CUSTOMER_ID,TOTAL) VALUES(%s,%s)
                    """,(account_id,0))


    except mysql.connector.Error as err:
        print(f"SQL Error {err}")
    finally:
        conn.commit()
        conn.close()
        return account_id


def deposit(cus_id,amt):
    global conn
    try:
        conn = DB_connection()
        cur = conn.cursor()
        cur.execute("""
                    UPDATE ACCOUNT
                    SET TOTAL = TOTAL +%s
                    WHERE CUSTOMER_ID =%s;
        """,(amt,cus_id))
        cur.execute("""
                    SELECT ACCOUNT_ID 
                    FROM ACCOUNT
                    WHERE CUSTOMER_ID = %s;
                    """,(cus_id,))
        acc_id = cur.fetchall()[0][0]
        cur.execute("""
                    INSERT INTO TRANSCATION
                    (ACCOUNT_ID,TYPE,AMOUNT) VALUES
                    (%s,%s,%s)
                    """,(acc_id,"Deposit",amt))
        print(f"AMMOUNT DEPOSIT SUCESSFULLY :{amt}")
    except mysql.connector.Error as err:
        print(f"SQL ERROR {err}")

    finally:
        conn.commit()
        conn.close()

def withdraw(cus_id,amt):
    global conn
    try:
        conn = DB_connection()
        cur = conn.cursor()
        cur.execute("""
                SELECT TOTAL FROM ACCOUNT WHERE CUSTOMER_ID = %s
                """,(cus_id,))
        total = cur.fetchall()[0][0]
        if not total < amt:
            cur.execute("""
                        UPDATE ACCOUNT
                        SET TOTAL = TOTAL -%s
                        WHERE CUSTOMER_ID =%s;
            """,(amt,cus_id))
            cur.execute("""
                        SELECT ACCOUNT_ID 
                        FROM ACCOUNT
                        WHERE CUSTOMER_ID = %s;
                        """,(cus_id,))
            acc_id = cur.fetchall()[0][0]
            cur.execute("""
                        INSERT INTO TRANSCATION
                        (ACCOUNT_ID,TYPE,AMOUNT) VALUES
                        (%s,%s,%s)
                        """,(acc_id,"WITHDRAW",amt))
            print(f"WITHDRAW SUCESSFULLY {amt}")
        else:
            print("Insuffient Amount")
    except mysql.connector.Error as err:
        print(f"SQL ERROR {err}")

    finally:
        conn.commit()
        conn.close()



def transccation(cus_id):
    global con
    try:
        con = DB_connection()
        cur = con.cursor()
        cur.execute("""
                        SELECT ACCOUNT_ID 
                        FROM ACCOUNT
                        WHERE CUSTOMER_ID = %s;
                        """,(cus_id,))
        acc_id = cur.fetchall()[0][0]
        cur.execute("""
                    SELECT * FROM TRANSCATION WHERE ACCOUNT_ID = %s
                    """,(acc_id,))

        tran = cur.fetchall()
        print("TRANS_ID\t ACC_ID \t TYPE \t\t\tAMOUNT")
        for i in tran:
            for j in i:
                print(j,end="\t\t\t")
            print("")
        cur.execute("""
                    SELECT TOTAL FROM ACCOUNT WHERE ACCOUNT_ID = %s    
                        """,(acc_id,))
        tot = cur.fetchall()[0][0]

        print(f"_________________TOTAL_________________{tot}")
    except mysql.connector.Error as err:
        print(f"SQL ERROR {err}")
    finally:
        con.commit()
        con.close()



def bal(cus_id):
    global con, cur
    try:
        con = DB_connection()
        cur = con.cursor()
        cur.execute("""
                        SELECT TOTAL 
                        FROM ACCOUNT
                        WHERE CUSTOMER_ID = %s;
                        """,(cus_id,))
        TOT = cur.fetchall()[0][0]
        print(f"TOTAL:{TOT}")
    except mysql.connector.Error as err:
        print(f"SQL ERROR {err}")
    finally:
        con.commit()
        cur.close()



