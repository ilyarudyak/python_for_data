import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

# TODO: process results
format_string = "[$%s]\n%s\n%s\n"
[print(format_string % (value, text, answer)) for (text, answer, value) in results]

connection.close()
