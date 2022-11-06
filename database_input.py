# create a loop to collect informations of all student
import sqlite3
# CRUD = create, read, update, Delete


connection = sqlite3.connect("student_registration.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE if not exists student_info (id INT, name TEXT, age FLOAT, height FLOAT NOT NULL, state VARCHAR(30), date_of_birth TEXT) """)


for x in range(2):
    print("input your name")
    name = input("")

    print("input your age")
    age = float(input(""))

    print("input your height")
    height = float(input(""))

    print("input your state")
    state = input("")

    print("input your Date of birth format '03:09:1920' ")
    birth = input("")

    cursor.execute("""INSERT INTO student_info (name, age, height, state, date_of_birth)
    VALUES (?, ?, ?, ?, ?)""", (name, age, height, state, birth))

connection.commit()
connection.close()
