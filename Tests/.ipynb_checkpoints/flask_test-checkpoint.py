'''
CS257: Software Design
Flask Individual Deliverable
Hilly Gangolf
Spring 2026

flask_test.py: A program for testing app.py
Some starter code taken from flask intro lab
'''

from app import *
import unittest

class TestSOMETHING(unittest.TestCase): 

    def test_route(self):
        """ This function tests that the homepage works properly """
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/', follow_redirects=True) 
        #TestResponse has webpage in .data
        text = response.get_data(as_text=True)

        # Check that certain sentences appear
        self.assertIn("Welcome to the Art Tracker", text)
        self.assertIn("To find stolen count by a given artist", text)
        self.assertIn("/artist/ARTIST_NAME", text)

    def return_artwork_given_origin(self):
        """ ADD COMMENT """
        self.app = app.test_client() 
        response = self.app.get('/origin/France', follow_redirects=True)
        self.assertEqual(b'The number of works that have been stolen from France is 10', response.data)

    def return_artwork_given_artist(self):
        """ ADD COMMENT """
        self.app = app.test_client() 
        response = self.app.get('/artist/Claude Monet', follow_redirects=True)
        # Check that certain artworks appear
        self.assertIn("Reflections On Water", reponse)
        self.assertIn("The Plain Of Gennevillers", reponse)
        self.assertIn("Torrent De La Creuse", reponse)

    def test_page_not_found(self):
        """ This function tests that 404 error returns the correct message """
        self.app = app.test_client() 
        response = self.app.get('/adfadfadf', follow_redirects=True)
        self.assertEqual(b"Sorry, wrong format. Check your Spelling", response.data )

if __name__ == '__main__':
    unittest.main()
