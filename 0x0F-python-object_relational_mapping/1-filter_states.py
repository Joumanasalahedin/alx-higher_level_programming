#!/usr/bin/python3
"""List all states starting with N from hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(
        "Select * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    states = cur.fetchall()

    for state in states:
        print(state)
    cur.close()
    db.close()
