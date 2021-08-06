#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    users = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(host="localhost",port=3306,user=users,
                  passwd=password,db=database, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT states.id, name FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print (row)
    cursor.close()
    db.close()