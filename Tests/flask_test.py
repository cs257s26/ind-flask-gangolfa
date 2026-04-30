'''
CS257: Software Design
Flask Individual Deliverable
Hilly Gangolf
April 29, 2026

flask_test.py: A program for testing app.py
Some starter code taken from flask intro lab
'''

from app import *
import unittest

class TestSOMETHING(unittest.TestCase): 

    # This function tests that the homepage works properly
    def test_route(self):
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/', follow_redirects=True) 
        #TestResponse has webpage in .data
        text = response.get_data(as_text=True)

        # Check that certain sentences appear
        self.assertIn("Welcome to the Art Tracker", text)
        self.assertIn("To find stolen count by a given artist", text)
        self.assertIn("/artist/[ARTIST_NAME]", text)
    
    # This function tests that get_count_stolen_by_artist returns the correct value
    def test_get_count_stolen_by_artist(self):
        self.app = app.test_client() 
        response = self.app.get('/artist:Andy Warhol', follow_redirects=True)
        self.assertEqual(b'The number of Andy Warhol works that have been stolen is 40', response.data )

    # This function tests that get_creator returns the correct value
    def test_get_creator(self):
        self.app = app.test_client() 
        response = self.app.get('/artwork:Mickey Mouse', follow_redirects=True)
        self.assertEqual(b'The creator of Mickey Mouse is Andy Warhol', response)

    # This function tests that 404 error returns the correct message
    def test_page_not_found(self):
        self.app = app.test_client() 
        response = self.app.get('/adfadfadf', follow_redirects=True)
        self.assertEqual(b"Sorry, wrong format. Check your Spelling", response.data )

if __name__ == '__main__':
    unittest.main()
