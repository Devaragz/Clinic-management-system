import sys
from database import setup_database
from auth import create_account, login
from operations import handle_operations


def main():
    conn = setup_database()
    cur = conn.cursor()

    while True:
        print("--- Dental Management ---")
        print("1. Login | 2. Create Account | 3. Exit")
        opt = input("Choice: ")

        if opt == '1':
            if login(conn, cur):
                handle_operations(conn, cur)
        elif opt == '2':
            create_account(conn, cur)
        elif opt == '3':
            conn.close()
            sys.exit()


if __name__ == "__main__":
    main()