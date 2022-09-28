import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="emp")
mycursor = mydb.cursor()
mycursor.execute("select * from emp_system")

for i in mycursor:
    print(i)