#!/usr/bin/python3
"""List all cities of a state from database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities 
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4], ))

    cities = cur.fetchall()
    c = list(city[0] for city in cities)
    print(*c, sep=", ")

    cur.close()
    db.close()
