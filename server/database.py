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

##### TABLE CREATION #####
# conn.execute('''CREATE TABLE student (studentId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         name CHAR(255) NOT NULL,
#                                         username VARCHAR(8) NOT NULL,
#                                         password TEXT NOT NULL);''')
# conn.execute('''CREATE TABLE teacher (teacherId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         name CHAR(255) NOT NULL,
#                                         username VARCHAR(8) NOT NULL,
#                                         password TEXT NOT NULL);''')
# conn.execute('''CREATE TABLE course (courseId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         code VARCHAR(8) NOT NULL,
#                                         description TEXT NOT NULL);''')
# conn.execute('''CREATE TABLE section (sectionId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         number CHAR(1) NOT NULL,
#                                         courseId INTEGER NOT NULL,
#                                         teacherId INTEGER NOT NULL,
#                                         FOREIGN KEY (courseId) REFERENCES course(courseId),
#                                         FOREIGN KEY (teacherId) REFERENCES teacher(teacherId));''')
# conn.execute('''CREATE TABLE enrollment (enrollmentId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         sectionId INTEGER NOT NULL,
#                                         studentId INTEGER NOT NULL,
#                                         FOREIGN KEY (sectionId) REFERENCES section(sectionId),
#                                         FOREIGN KEY (studentId) REFERENCES student(studentId));''')
# conn.execute('''CREATE TABLE quiz (quizId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         number INTEGER NOT NULL,
#                                         sectionId INTEGER NOT NULL,
#                                         FOREIGN KEY (sectionId) REFERENCES section(sectionId));''')
# conn.execute('''CREATE TABLE question (questionId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         number INTEGER NOT NULL,
#                                         text TEXT NOT NULL,
#                                         quizId INTEGER NOT NULL,
#                                         FOREIGN KEY (quizId) REFERENCES quiz(quizId));''')
# conn.execute('''CREATE TABLE option (optionId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         number INTEGER NOT NULL,
#                                         text TEXT NOT NULL,
#                                         correct INTEGER NOT NULL,
#                                         questionId INTEGER NOT NULL,
#                                         FOREIGN KEY (questionId) REFERENCES question(questionId));''')
# conn.execute('''CREATE TABLE submission (submissionId INTEGER PRIMARY KEY AUTOINCREMENT,
#                                         studentId INTEGER NOT NULL,
#                                         optionId INTEGER NOT NULL,
#                                         FOREIGN KEY (studentId) REFERENCES student(studentId),
#                                         FOREIGN KEY (optionId) REFERENCES option(optionId));''')

# conn.execute("""INSERT INTO student (name, username, password)
#                             VALUES (?, ?, ?);""", ('Mohammad Usman', '20-10558', sha_signature))
# conn.execute("""INSERT INTO student (name, username, password)
#                             VALUES (?, ?, ?);""", ('Danish Ali', '20-10572',  sha_signature))

# conn.execute("""INSERT INTO quiz (number)
#                             VALUES (?);""", (1,))

# conn.execute("""INSERT INTO question (number, question, quizId)
#                             VALUES (?, ?, ?);""", (1, 'What is the factorial of 5?', 1))
# conn.execute("""INSERT INTO question (number, question, quizId)
#                             VALUES (?, ?, ?);""", (2, 'What is the factorial of 4?', 1))

# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (1, '120', 1, 1))
# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (2, '256', 0, 1))
# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (3, '24', 0, 1))
# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (4, '1', 0, 1))

# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (1, '120', 0, 2))
# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (2, '256', 0, 2))
# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (3, '24', 1, 2))
# conn.execute("""INSERT INTO option (number, option, correct, questionId)
#                             VALUES (?, ?, ?, ?);""", (4, '1', 0, 2))

conn.commit()  # commit any changes made

# username = "20-10558"
# cursor = conn.execute(
#     """SELECT * FROM student WHERE username = (?);""", [username])
# for row in cursor:
#     print("StudentId = ", row[0])
#     print("Name = ", row[1])
#     print("Username = ", row[2])
#     print("Password = ", row[3], "\n")

conn.close()  # close database connection
