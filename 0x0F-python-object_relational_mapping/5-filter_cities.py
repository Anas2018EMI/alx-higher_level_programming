#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        """SELECT cities.name FROM cities JOIN states
        ON cities.state_id = states.id WHERE states.name = %s
        ORDER BY cities.id
""", (argv[4],))
    rows = cur.fetchall()
    i = 0
    if len(rows) > 0:
        for i in range(len(rows) - 1):
            print(f"{rows[i][0]}, ", end='')

        print(rows[i+1][0])
    cur.close()
    db.close()
