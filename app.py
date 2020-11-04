import dbcreds
import mariadb

conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
cursor = conn.cursor()

def insert_post(username, content):
    cursor.execute("INSERT INTO blog_post(username, content, id) VALUES(?, ?, NULL)", [username, content])
    conn.commit()
def select_post():
    cursor.execute("SELECT * FROM blog_post")
    rows = cursor.fetchall()
    conn.commit()
    print(rows)
    for row in rows:
        print(row[1])

def game_check():
    check = input("would you like to continue? Y/N: ")
    if check == "Y":
        return True
    elif check == "N":
        return False

def check_login(username):
    cursor.execute("SELECT * FROM users")
    user_rows = cursor.fetchall()
    conn.commit()
    print(user_rows)
    for user_row in user_rows:
        print(user_row[0])
        if username == user_row[0]:
            return True
        else:
            return False
            

print("Welcome to the blog site.")
username = input("Please input your username: ")
password = input("Please input your password: ")

login_verify = check_login(username)
if login_verify == True:
    print("Hi " + username + ", please select from the following options: ")
    print("1: Write a new post")
    print("2: See all other posts")
    userSelection = input()

    while True:
        if userSelection == "1":
            content = input("Please write a new post: ")
            insert_post(username, content)
            check_continue = game_check()
            if check_continue == False:
                print("Goodbye!")
                break
        elif userSelection == "2":
            select_post()
            check_continue = game_check()
            if check_continue == False:
                print("Goodbye!")
                break
        else:
            print("You have invalid selection, please select again.")
            break
elif login_verify == False:
    print("Sorry, you haven't registered yet!")

cursor.close()
conn.close()