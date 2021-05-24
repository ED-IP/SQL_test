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
        rows = [("Bob", 78, "1990-02-07 12:12:12"),
                ("Joe", 25, "1999-08-01 17:14:30"),
                ("Hicks", 18, "1900-04-10 01:02:03")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

   