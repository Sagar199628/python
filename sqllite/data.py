import mysql.connector

def adddata():
    name = e1.get()
    email = e2.get()
    password = e3.get()

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        port = 3306,
        database = "1feb_python"
    )
    cursor = mydb.cursor()

