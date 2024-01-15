#!/usr/bin/python3
"""
a script that takes in the name of a
state as an argument and lists all
cities of that state
Results must be sorted in
ascending order by cities.id
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    Accessing the data base
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM cities JOIN\
                 ON cities.state_id = states.id\
                 ORDER BY cities.id")
    [print(", ".join([c[2] for c in curr.fetchall() if c[4] == argv[4]]))]

    curr.close()
    db.close()
