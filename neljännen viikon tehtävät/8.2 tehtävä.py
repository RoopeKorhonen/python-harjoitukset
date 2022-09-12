import mysql.connector
"SELECT type, COUNT*) AS FROM airport WHERE iso_country * 'SE' GROUP BY TYPE"

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='moodleroope',
         autocommit=True
         )
maakoodi = input("Anna 2 kirjaiminen maakoodi")
sql = "SELECT name, continent FROM country WHERE iso_country = '" + maakoodi +"'"
print(sql)

sgl = "SELECT name FROM country"
cursor = yhteys.cursor()
cursor.execute(sgl)
result = cursor.fetchall()
for rivi in result:
    print(result[0])