
import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'akolo000',
)

cursor = dataBase.cursor()

cursor.execute('CREATE DATABASE django_crm')


