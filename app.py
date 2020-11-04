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

def exit_check():
    check = input("would you like to continue? Y/N: ")
    if check == "N":
        return True
    elif check == "Y":
        return False


def login_check(username, password):
    cursor.execute("SELECT * FROM users")
    user_rows = cursor.fetchall()
    conn.commit()
    # print(user_rows)
    for user_row in user_rows:
        # print(user_row[0])
        if username == user_row[0] and password == user_row[1]:
            return True
    return False         

print("Welcome to the blog site.")
while True:
    print("Have you registered? Y/N")
    registration = input()
    if registration == "N":
        pass
    elif registration == "Y":
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if login_check(username, password):
            while True: 
                print("Hi " + username + ", please select from the following options: ")
                print("1: Write a new post")
                print("2: See all other posts")
                userSelection = input()
                if userSelection == "1":
                    content = input("Please write a new post: ")
                    insert_post(username, content)
                elif userSelection == "2":
                    select_post()
                else:
                    print("You have invalid selection, please select again.")
                if exit_check():
                    print("Goodbye!")
                    break
            break     
        else: 
            print("Sorry, your password is not correct, please try it again.")

cursor.close()
conn.close()