import mysql.connector 
from decouple import config

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd =  config('DATABASE_PASSWORD', default=''),
)
# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crm_app_db")

print("Done & Done !") 