#!/usr/bin/python3
""" But this time, write one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    users = argv[1]
    password = argv[2]
    database = argv[3]
    argument = argv[4]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=users,
        passwd=password, db=database, charset="utf8")
    cursor = db.cursor()
    cursor.exucute("SELECT states.id, name FROM states WHERE\
        name LIKE BINARY %s ORDER BY \
        states.id ASC", (argument, ))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
