import os
import datetime
import pymysql

# Get username from Gitpod

username = os.getenv("C9_USER")

# Connect to the database
connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")


try:
    # Run a Query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-3-5 16:45:18"),
                ("Joe", 34, "1979-1-10 06:35:20"),
                ("Alan", 60, "1950-3-5 23:20:05")]
        cursor.executemany("INSERT INTO Friends VALUES(%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()