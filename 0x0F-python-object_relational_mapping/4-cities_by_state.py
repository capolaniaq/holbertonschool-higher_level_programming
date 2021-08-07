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
    sql = ("SELECT cities.id, cities.name, states.name FROM \
        cities JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")
    cursor.exucute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()