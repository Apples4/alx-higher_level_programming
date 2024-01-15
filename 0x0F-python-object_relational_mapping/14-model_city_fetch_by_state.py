#!/usr/bin/python3
"""
Write a Python file similar to model_state.py
named model_city.py that contains
the class definition of a City.
"""

from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_pring=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
