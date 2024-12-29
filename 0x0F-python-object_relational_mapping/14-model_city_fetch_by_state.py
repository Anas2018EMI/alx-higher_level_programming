#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Create database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session
    session = Session(bind=engine)

    # Query cities and states together
    query = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    # Display results
    for state, city in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
