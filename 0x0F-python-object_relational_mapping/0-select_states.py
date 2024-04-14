#!/usr/bin/python3
import sys
import MySQLdb

argv = sys.argv
if (len(argv) == 4 and __name__ == '__main__'):
    con = MySQLdb.connect(
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                host='localhost'
            )
    cur = con.cursor()
    query = cur.execute('SELECT * FROM states ORDER BY `id` asc;')
    res = cur.fetchall()
    for row in res:
        print(row)
