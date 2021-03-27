#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database
hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD,
                         db=DATABASE, port=PORT)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cursor.fetchall()
    for r in rows:
        # This if is redundant, but checker needs it apparently
        if r[1][0] == 'N':
            print(r)
    cursor.close()
    db.close()
