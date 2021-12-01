import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')

    cursor = sqlite_connection.cursor()
#    cursor.execute('''CREATE TABLE test (
#                                id INTEGER PRIMARY KEY,
#                                val REAL NOT NULL);''')
    cursor.execute('''insert into test (id, val) values (3, 3.1), (2, 31.1), (4, 31.1);''')
    cursor.execute('''select * from test where id>0;''')
    rows = cursor.fetchmany(size=3)
    print(rows)
    sqlite_connection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

