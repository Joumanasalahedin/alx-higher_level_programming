#!/usr/bin/python3
"""List all cities from database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
