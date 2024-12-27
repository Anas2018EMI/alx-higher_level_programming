#!/usr/bin/python3
"""
    all states with a name starting with N from the hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states_starting_with_N(username, password, database):
    """
    Lists all states with a name starting with N from the db hbtn_0e_0_usa
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select states starting with 'N'
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    list_states_starting_with_N(username, password, database)
