import os
import sys
import mysql.connector as sql
from dotenv import load_dotenv

load_dotenv() # Loads the secrets from .env

def get_connection(use_db=True):
    try:
        if use_db:
            return sql.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'),
                               passwd=os.getenv('DB_PASS'), database=os.getenv('DB_NAME'))
        return sql.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASS'))
    except sql.Error as err:
        print(f"Database Error: {err}")
        sys.exit()

def setup_database():
    conn = get_connection(use_db=False)
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
    conn.close()

    conn = get_connection(use_db=True)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS patient_record (
                    Patient_Name VARCHAR(50), Age INT, Doctor_Consulted VARCHAR(50), 
                    Address VARCHAR(150), Phone_Number BIGINT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS salary_record (
                    Employee_Name VARCHAR(50), Profession VARCHAR(20), 
                    Salary_Amount INT, Address VARCHAR(150), Phone_Number BIGINT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS accounts (
                    User_Name VARCHAR(20) PRIMARY KEY, Password VARCHAR(255))''')
    conn.commit()
    return conn