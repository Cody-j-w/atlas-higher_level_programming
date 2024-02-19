#!/usr/bin/python3

"""
filter_cities - run a filtered query on a mysql DB using the MySQLdb
module, to find all cities of a provided state
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

    query = """SELECT cities.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id;"""

    staterows = cur.execute(query, (state,))
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end=", " if i < len(rows) - 1 else "\n")
