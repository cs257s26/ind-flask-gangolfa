'''
CS257: Software Design
Flask Individual Deliverable
Hilly Gangolf
April 29, 2026

app.py: A program for building a flask application
Some starter code taken from flask intro lab
'''

from flask import Flask
from ProductionCode.command_line import *
import csv

app = Flask(__name__)

# This is the home page
# Returns a list of instructions for running searches
@app.route('/')
def homepage():
    instructions = """
    <h1>Welcome to the Art Tracker</h1>
    <p>1. To find stolen count by a given artist, enter: <br>
    http://127.0.0.1:5100/artist/[ARTIST_NAME]</p>
    
    <p>2. To find artist of a given artwork, enter: <br>
    http://127.0.0.1:5100/artwork/[ARTWORK_TITLE]</p>
    """
    return instructions

# This route is used to call count_stolen_by_artists() function
# Returns a string including the number of stolen works
@app.route('/artist:<string:artist>')
def get_count_stolen_by_artist(artist:str) -> int:
    return f"The number of {artist} works that have been stolen is " + str(count_stolen_by_artist(artist))

# This route is used to call find_creator() function
# Returns a string includig the creator of an artwrork
@app.route('/artwork:<string:artwork>')
def get_creator(artwork: str):
    return f"The creator of {artwork} is " + find_creator(artwork)

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
    app.run(port=5100)