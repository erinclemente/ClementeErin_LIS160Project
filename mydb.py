import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user= 'root',
	passwd = 'Nire.1sk0'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE erinclemente")

print("All Done!")