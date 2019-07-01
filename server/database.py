import sqlite3
import hashlib


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


# hash_string = 'password'
# sha_signature = encrypt_string(hash_string)
# print(sha_signature)

conn = sqlite3.connect('test.db')
# print("Opened database successfully")

# conn.execute('''CREATE TABLE student (studentId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         name CHAR(255) NOT NULL,
#                                         username VARCHAR(8) NOT NULL,
#                                         password TEXT NOT NULL);''')

# conn.execute("""INSERT INTO student (name, username, password)
#                             VALUES (?, ?, ?);""", ('Mohammad Usman', '20-10558', sha_signature))
# conn.execute("""INSERT INTO student (name, username, password)
#                             VALUES (?, ?, ?);""", ('Danish Ali', '20-10572',  sha_signature))
# conn.commit()  # commit any changes made

username = "20-10558"
cursor = conn.execute(
    """SELECT * FROM student WHERE username = (?);""", [username])
for row in cursor:
    print("StudentId = ", row[0])
    print("Name = ", row[1])
    print("Username = ", row[2])
    print("Password = ", row[3], "\n")

conn.close()  # close database connection
