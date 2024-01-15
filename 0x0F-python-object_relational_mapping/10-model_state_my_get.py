#!/usr/bin/python3
"""
Write a script that prints the State object
with the name passed as argument from the database
"""

from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_pring=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    is_here = False
    for state in session.query(State):
        if state.name == argv[4]:
            print('{}'.format(state.id))
            is_here = True
            break
    if is_here is False:
        print("Not found")
