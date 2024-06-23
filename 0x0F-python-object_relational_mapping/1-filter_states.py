#!/usr/bin/python3
"""Module for Select State Database"""

import MySQLdb
import sys


def main():
    db_username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=db_username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
