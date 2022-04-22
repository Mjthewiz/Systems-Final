import sqlite3 as sql

conn = sql.connect ("database.db")

conn.execute ("CREATE TABLE Shirts(Name TEXT, Size TEXT, Color Text)")

conn.close()

print ("Done")