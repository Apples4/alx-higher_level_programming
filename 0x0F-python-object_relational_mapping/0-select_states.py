#!/usr/bin/python3
"""
Write a script that lists all states
from the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Accessing the database
    """
    db = MySQLdb.connnect(host="localhost",
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT *FROM states ORDER BY id")
    [print(state) for state in cur.fetchall()]
