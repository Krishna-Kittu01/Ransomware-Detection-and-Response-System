import sqlite3

conn = sqlite3.connect("data/rdrs.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM file_events")

rows = cursor.fetchall()

print("\nStored Events:\n")

for row in rows:
    print(row)

conn.close()