'''
CS257: Software Design
Database Individual Deliverable
Hilly Gangolf
April 29, 2026

appSQL.py: A program for building a flask application
Some starter code taken from flask intro lab
'''

from flask import Flask
from ProductionCode.data.datasource import *
import csv
import sys

app = Flask(__name__)

# This is the home page
# Returns a list of instructions for running searches
@app.route('/')
def homepage():
    instructions = """
    <h1>Welcome to the Art Tracker</h1>
    <p>1. To find stolen count by a given artist, enter: <br>
    http://[port number]/artist/ARTIST_NAME</p>
    
    <p>2. To find artist of a given artwork, enter: <br>
    http://[port]/artwork/ARTWORK_TITLE</p>
    """
    return instructions

# This route is used to call count_stolen_by_artists() function
# Returns a string including the number of stolen works
@app.route('/origin/<string:origin>')
def get_artwork_given_origin(origin:str) -> int:
    connection = connect()
    return f"The number of works that have been stolen from {origin} is " + str(get_artwork_given_origin(connection, origin))

# This route is used to call find_creator() function
# Returns a string including the creator of an artwrork
@app.route('/artist/<string:artist>')
def get_artwork_given_artist(connection, artist: str):
    connection = connect()
    return f"{artist} is the creator of" + get_artwork_given_artist(connection, artist)

# This route is used to handle page_not_found errors
# It returns a string with helpful advice for the user
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry, wrong format. Check your Spelling"

# This route is used to handle additional python errors
# It returns a string with helpful advice for the user
@app.errorhandler(500)
def python_bug(e):
    return "Something went wrong in our Python code"

if __name__ == '__main__':
    # Default port if none is provided
    port = 5000 
    
    # Check if an argument was passed
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Port must be a valid integer. Using default port 5000.")

    app.run(port=port, host="stearns.mathcs.carleton.edu")