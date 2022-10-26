import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "varoo",
        password = "varoo",
        database = "backend"
)

cursor = mydb.cursor()

import random

first_names=('Jack','Amy','Joe', 'Arjun', 'Rahul', 'Arnav', 'Pritika')
last_names=('Johnson','Smith','TukaRam', 'Rai', 'Sharma', 'Kohli', 'Kapoor')

genre = ("Allergists", "Anesthesiologists", "Cardiologists", "Critical Care Medicine Specialists")


for _ in range(10):
    rating = random.randint(1,4) + random.random()
    cursor.execute("insert into doctors(name, genre,rating) values(%s, %s, %s)", ("".join(random.choice(first_names) + " " + random.choice(last_names)), random.choice(genre), rating))


mydb.commit()
