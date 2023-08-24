# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE IF NOT EXISTS Students (
Student_Id INTEGER NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY);"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
(201,'Иван',1),
(202,'Петр',2),
(203,'Анастасия',3),
(204,'Игорь',4) ON CONFLICT DO NOTHING;"""
cursor.execute(query)
connection.commit()
connection.close()


connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
def info_student_id(Student_Id):
  try:
    query_id ="""select Students.student_id, Students.Student_Name, School_id, School.School_Name
              from Students
              JOIN School USING (School_id)
              WHERE Students.student_id = ?;"""
    cursor.execute(query_id, (Student_Id,))
    result = cursor.fetchone()
    print(f' ID Студента: {result[0]}\n Имя студента: {result[1]}\n' 
          f' ID школы: {result[2]}\n Название школы: {result[3]}\n')

  except (Exception, sqlite3.Error):
    print ('Студента с таким ID нет')

info_student_id(204)