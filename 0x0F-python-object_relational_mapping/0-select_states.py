#!/usr/bin/python3
""" list all cities from database """

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
    query = cur.execute('SELECT * FROM states ORDER BY `id` asc;')
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    con.close()
