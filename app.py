'''
CS257: Software Design
Flask Individual Deliverable
Hilly Gangolf
Spring 2026

app.py: A program for building a flask application
Some starter code taken from flask intro lab
'''

from flask import Flask
from ProductionCode.command_line import *
import csv
import sys

app = Flask(__name__)

# This is the home page
@app.route('/')
def homepage():
    """When one accesses the webpage at / this funciton displays
    Args:
        None
    Returns:
        string: A string containing directions for website"""
    
    instructions = """
    <h1>Welcome to the Art Tracker</h1>
    <p>1. To find stolen count by a given artist, enter: <br>
    http://[Host][Port]/artist/ARTIST_NAME</p>
    
    <p>2. To find artist of a given artwork, enter: <br>
    http://[Host][Port]/artwork/ARTWORK_TITLE</p>
    """
    return instructions

# This route is used to call count_stolen_by_artists() function
@app.route('/artist/<string:artist>')
def get_count_stolen_by_artist(artist:str) -> int:
    """Returns a string including the number of stolen works
    Args:
        artist (str): Name of artist
    Returns:
        int: count of artworks that a given artist has had stolen"""
    
    return f"The number of {artist} works that have been stolen is " + str(count_stolen_by_artist(artist))

# This route is used to call find_creator() function
@app.route('/artwork/<string:artwork>')
def get_creator(artwork: str):
    """Returns a string including the creator of an artwrork
    Args:
        artwork (str): Name of artwork
    Returns:
        str: name of artist"""
    
    return f"The creator of {artwork} is " + find_creator(artwork)

@app.errorhandler(404)
def page_not_found(e):
    """Used to handle page_not_found errors. This function returns a string with helpful advice for the user
    Args:
        e (int): this param is handled automatically by the decorator
    Returns:
        str: an error string"""
    
    return "Sorry, wrong format. Check your Spelling"

# Additional python errors
@app.errorhandler(500)
def python_bug(e):
    """This function returns a string with helpful advice for the user
    Args:
        e (int): this param is handled automatically by the decorator
    
    Returns:
        str: an error string"""
    
    return "Something went wrong in our Python code"

if __name__ == '__main__':
    app.run()