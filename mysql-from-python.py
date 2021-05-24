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
        rows = [(23, "Bob"),
                (26, "Alan"),
                (57, "Joe")]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()