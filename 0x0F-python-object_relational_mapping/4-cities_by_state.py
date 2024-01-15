#!/usr/bin/python3
"""
 a script that lists all cities
 from the database hbtn_0e_4_usa
 Results must be sorted in
 ascending order by cities.id
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    Accessing the database
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    curr = db.cursor()
    curr.execute("SELECT cities.id,\
                 cities.name,\
                 states.name FROM cities\
                 JOIN states ON cities.state_id\
                 ORDE BY cities.id")
    [print(cities) for cities in curr.fetchall()]

    curr.close()
    db.close()
