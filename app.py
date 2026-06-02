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

@app.route('/')
def homepage():
    instructions = """
    <h1>Welcome to the Art Tracker</h1>
    <p>1. To find stolen count by a given artist, enter: <br>
    http://[Host][Port]/artist/ARTIST_NAME</p>
    
    <p>2. To find artist of a given artwork, enter: <br>
    http://[Host][Port]/artwork/ARTWORK_TITLE</p>
    """
    return instructions

@app.route('/origin/<string:origin>')
def return_artwork_given_origin(origin:str) -> int:
    connection = connect()
    result = str(get_artwork_given_origin(connection, origin)[0][0])
    return f"The number of works that have been stolen from {origin} is " + result


@app.route('/artist/<string:artist>')
def return_artwork_given_artist(artist: str):
    connection = connect()
    result = get_artwork_given_artist(connection, artist)
    titles = [item[0] for item in result]

    return f"The following works by {artist} have been stolen: <br>" + "<br>".join(titles)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry, wrong format. Check your Spelling"

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