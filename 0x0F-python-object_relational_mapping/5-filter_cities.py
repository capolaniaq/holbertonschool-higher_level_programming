#!/usr/bin/python3
""" But this time, write one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    users = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=users,
        passwd=password, db=database, charset="utf8")
    cursor = db.cursor()
    sql = ("""SELECT cities.name FROM cities JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id""")
    argument = (argv[4], )
    cursor.execute(sql, argument)
    results = cursor.fetchall()
    for x, row in enumerate(results):
        if x == len(results) - 1:
            print("{}".format(row[0]))
        else:
            print("{}".format(row[0]), end=', ')
    cursor.close()
    db.close()
