#!/usr/bin/python3
"""
SQL injection
script should take 4 arguments
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
    curr.execute("SELECT * FROM states WHERE
                 name=%s ORDER BY id ASC",
                 (sys.argv[4],))
    [print(states) for states in curr.fetchall()]

    curr.close()
    db.close()
