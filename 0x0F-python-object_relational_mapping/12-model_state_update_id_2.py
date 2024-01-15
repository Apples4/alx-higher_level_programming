#!/usr/bin/python3
"""
Write a script that changes the name of a
State object from the database
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

    up_state = session.query(State).filter_by(id=2).first()
    up_state.name = 'New Mexico'
    session.commit()
