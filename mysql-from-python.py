import os
import pymysql

# Get username from Cloud9 environment
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            #removed '' from 'username'
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print (result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
    
    
        