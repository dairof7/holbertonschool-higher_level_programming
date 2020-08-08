#!/usr/bin/python3
""" print all states start by N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    STATE = sys.argv[4]

    MY_HOST = "localhost"

    db = MySQLdb.connect(
        host=MY_HOST,
        port=3306,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB)

    cur = db.cursor()

    cur.execute("SELECT cities.name \
    FROM states JOIN cities ON states.id = cities.state_id \
    WHERE states.name=%s \
    ORDER BY 'cities.id';", (STATE,))
    rows = cur.fetchall()
    i = 1
    for row in rows:
        if (i == 1):
            print("{:}".format(row[0]), end='')
            i = 0
        else:
            print(", ", end='')
            print("{:}".format(row[0]), end='')
    print("")
    cur.close()
    db.close()
