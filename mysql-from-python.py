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
        rows = [("Rich", 21, "1997-02-08 22:22:15"),
                ("Dan", 45, "1977-05-04 10:25:50"),
                ("Archebald", 82, "1943-09-09 09:46:43")]
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob'")
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    connection.close()