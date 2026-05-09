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

def get_artwork_given_origin(connection, origin: str) -> list:
    """Retrieves all artwork (and all the other information associated with an artwork and its artist) given the artist's country of origin.

    Args:
        connection (psycopg2.connection) - the connection to the database
        origin (str) - the country of origin

    Returns:
        list - a list of all artwork with an artist from the desired origin.
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
        artist (str) - the artist being searched for

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

    # Execute a simple query: how many artists have an origin of the United Kingdom?
    results = get_artwork_given_origin(connection, 'United Kingdom')
    
    if results is not None :
        print()
        print("------------------ Origin Query results ------------------")
        print(results)
        print()

    # Execute a simple query: how many artists have an origin of the United Kingdom?
    results = get_artwork_given_artist(connection, 'Gustav Klimt')
    
    if results is not None :
        print("------------------ Artist Query results ------------------")
        print(results)

    # Disconnect from database
    connection.close()

main()