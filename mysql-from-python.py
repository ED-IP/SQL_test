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
        cursor.execute("DELETE FROM Friends WHERE name in ('bob', 'Joe')")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()