#!/usr/bin/python3
"""Module for Select State Database"""

import MySQLdb
import sys


if __name__ == "__main__":

    db_username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        user=db_username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    city_names = [row[1] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
