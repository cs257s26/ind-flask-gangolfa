"""psycopg2-sample.py

Sample code demonstrating how to use the psycopg2 Python library to 
connect to a database and execute a query.
"""

import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_artists_given_origin(connection, origin: str) -> list:
    """Retrieves all artists (and all the other information associated with an artist) given their country of origin.

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (float) - the minimum high temperature

    Returns:
        list - a list of all dates where the high temperature is greater or equal to temp, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM artist_data WHERE origin = %s;"
        cursor.execute(query, (origin,))
        return cursor.fetchall()
    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None
    
def get_artwork_given_artist(connection, artist: str) -> list:
    """Retrieves all artowrk (and all the other information associated with an artwork) given an artist.

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (float) - the minimum high temperature

    Returns:
        list - a list of artwork by a given artist.
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM interpol_data WHERE artist = %s;"
        cursor.execute(query, (artist,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_artists_given_origin(connection, 'United Kingdom')
    
    
    if results is not None :
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()