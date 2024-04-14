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
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    toList = list(row[0] for row in rows)
    print(*toList, sep=", ")
    cur.close()
    con.close()
