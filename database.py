import sqlite3
# CRUD = create, read, update, Delete


connection = sqlite3.connect("play_database.db")
cursor = connection.cursor()
# cursor.execute("""CREATE TABLE if not exists student_info (id INT, name TEXT, age FLOAT, complexion VARCHAR(10)) """)
# cursor.execute("""INSERT INTO student_info (id, name, age, complexion)
#  VALUES (1, 'Daniel Adeyemi', 15, 'Dark')""")
# cursor.execute("""INSERT INTO student_info (id, name, age, complexion)
#  VALUES (2, 'Dipo Adeyemi', 16, 'Fair')""")

# data = cursor.execute("""SELECT * FROM student_info""")
# data = cursor.execute("""SELECT name, age, complexion from student_info""")
# data = cursor.execute("""SELECT * FROM student_info WHERE name LIKE '%ni%' """)
# data = cursor.execute("""SELECT * FROM student_info WHERE name='di' """)



# for datas in data:
#     print(datas[1])
# cursor.execute("UPDATE student_info SET name='John Adeyemi' WHERE name='Benjamin Adeyemi'")
# cursor.execute("DELETE FROM student_info WHERE id=1")
cursor.execute("""CREATE TABLE if not exists teachers_table(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email VARCHAR(20) UNIQUE, institution TEXT, subject_taught VARCHAR(30))""")

cursor.execute("""INSERT INTO teachers_table(id, name, email, institution, subject_taught) VALUES
 (3, 'Bola', 'bola@gmail.com', 'Unilag', 'French')""")
cursor.execute("""INSERT INTO teachers_table(name, email, institution, subject_taught) VALUES
 ('Kenneth', 'keeth@gmail.com', 'Unilag', 'French')""")
cursor.execute("""INSERT INTO teachers_table(name, email, institution, subject_taught) VALUES
 ('Ola', 'fly@gmail.com', 'Unilag', 'French')""")
# cursor.execute("""INSERT INTO teachers_table(name, email, institution, subject_taught) VALUES
# ('', 'cole@gmail.com', 'Unilag', 'French')""")



# for datas in data:
#     print(datas[0])
#     print(datas[1])
#     print(datas[3])
connection.commit()
connection.close()
