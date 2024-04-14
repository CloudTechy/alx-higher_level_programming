#!/usr/bin/python3
""" filter cities from database """

import sys
import MySQLdb

argv = sys.argv
if (__name__ == '__main__'):
    con = MySQLdb.connect(
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                host='localhost',
                port=3306
            )
    cur = con.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY %s ORDER BY states.id""", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
