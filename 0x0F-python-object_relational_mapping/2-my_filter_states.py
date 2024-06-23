#!/usr/bin/python3
"""Module for Select State Database"""

import MySQLdb
import sys


if __name__ == "__main__":

    db_username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    n = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=db_username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name='{}'".format(n))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
