#!/usr/bin/python3

"""
select_states - run a query on a mysql DB using the MySQLdb module
"""

import MySQLdb
import sys


if __name__ == '__main__':

    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=user, passwd=pwd, db=database)
    cur = db.cursor()

    staterows = cur.execute("SELECT * FROM states ORDER BY states.id;")
    for row in cur._rows:
        print(row)
