#!/usr/bin/python3

"""
filter_states - run a filtered query on a mysql DB using the MySQLdb module
"""

import MySQLdb
import sys


if __name__ == '__main__':

    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=user, passwd=pwd, db=database)
    cur = db.cursor()

    staterows = cur.execute(
        """SELECT *
        FROM states
        WHERE name='{}'
        ORDER BY states.id;""".format(state)
        )
    for row in cur._rows:
        print(row)
