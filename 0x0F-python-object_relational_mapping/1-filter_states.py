#!/usr/bin/python3
"""
Write a script that lists all states
with a name starting with N
Results must be sorted in
ascending order by states.id
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Accessing the database

    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT *FROM states ORDER BY id")
    [print(state) for state in curr.fetchall() if state[1][0] == "N"]
