import dbcreds
import mariadb

print("Welcome to the blog site.")
username = input("Please input your username: ")
print("please select from the following options: ")
print("1: Write a new post")
print("2: See all other posts")

userSelection = input("Please enter your selection: ")

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

if userSelection == "1":
    content = input("Please write a new post: ")
    insert_post(username, content)
elif userSelection == "2":
    select_post()
else:
    print("You have invalid selection, please select again.")

cursor.close()
conn.close()