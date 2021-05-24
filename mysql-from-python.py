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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        row = ("Bob", 21, "1990-3-5 16:45:00")
        cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()