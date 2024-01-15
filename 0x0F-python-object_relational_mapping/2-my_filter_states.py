#!/usr/bin/python3
"""
Write a script that takes in an argument
and displays all values in the states
Results must be sorted in
ascending order by states.id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Accessing the database
    """
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'"
                .format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
