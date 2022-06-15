import sqlite3
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
command1 = """CREATE TABLE IF NOT EXISTS 
movies(movie_id INTEGER PRIMARY KEY, movie_title TEXT, actor_name TEXT,
 year INTEGER, director_name TEXT)"""
cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'shershah','siddharth_malhotra',2021,'vishnuvardhan')")
cursor.execute("INSERT INTO movies VALUES(2,'DDLJ','SRK',1995,'aditya_chopra')")
cursor.execute("INSERT INTO movies VALUES(3,'gadar','sunny_deol',2001,'anil_sharma')")
cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()
print(results)
print('Details of the movie in which SRK was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='SRK'")
res = cursor.fetchall()
print(res)