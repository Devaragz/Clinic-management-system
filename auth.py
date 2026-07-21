import bcrypt


def create_account(conn, cur):
    user = input("New User Name: ").strip().upper()
    password = input("New Password: ").strip()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cur.execute("INSERT INTO accounts (User_Name, Password) VALUES (%s, %s)", (user, hashed_pw.decode('utf-8')))
        conn.commit()
        print("Account added!\n")
    except Exception as e:
        print(f"Error (Username may exist): {e}\n")


def login(conn, cur):
    user = input('User Name: ').strip().upper()
    password = input('Password: ').strip()

    cur.execute("SELECT Password FROM accounts WHERE User_Name = %s", (user,))
    result = cur.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        print('\nLogin successful!\n')
        return True
    print('Invalid Credentials.\n')
    return False