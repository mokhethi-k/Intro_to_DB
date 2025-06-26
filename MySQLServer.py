from getpass import getpass
import mysql.connector

try:
    with mysql.connector.connect(
        host = "localhost",
        user = input("Enter username: "),
        password = input("Enter password: ")
    ) as connection:
        with connection.cursor() as mycursor:
            create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            mycursor.execute(create_database_query)
            print("Database 'alx_book_store' created successfully!")
            
except mysql.connector.Error as e:
    print(e)