import sqlite3

conn = sqlite3.connect("prospects.db")
c = conn.cursor()

c.execute("INSERT INTO distributors (username) VALUES (?)", ("admin",))

conn.commit()
conn.close()

print("Identifiant ajouté avec succès !")
