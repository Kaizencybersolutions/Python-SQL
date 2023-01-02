import mysql.connector

db= mysql.connector.connect(
	host="localhost",
	user="Roger",
	passwd="Roger",
	database="testdatabase"

)
mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("DESCRIBE Person")
#mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)",("Roger", 34))
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)",("Pau", 30))
db.commit()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
	print(x)
