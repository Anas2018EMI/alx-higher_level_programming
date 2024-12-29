#!/usr/bin/python3
"""Script that creates the State California with City San Francisco"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Create database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(bind=engine)

    # Create California state
    california = State(name="California")

    # Create San Francisco city
    san_francisco = City(name="San Francisco")

    # Add city to state's cities relationship
    california.cities.append(san_francisco)

    # Add state to session and commit
    session.add(california)
    session.commit()

    # Close the session
    session.close()
