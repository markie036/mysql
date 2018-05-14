import os
import datetime
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        row = ("Rich", 21, "1997-02-08 22:22:15")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    connection.close()