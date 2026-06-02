import unittest
from ProductionCode.command_line import *

class TestCommandLines(unittest.TestCase):

    def setUp(self):
        """Tests whether data from a valid CSV file is loaded successfully."""
        self.assertGreater(len(load_data(DEFAULT_DATA_PATH)), 0)
        self.assertGreater(len(load_data(ARTIST_DATA_PATH)), 0)

    def test_valid_find_creator(self):
        """ This function tests valid input for commandline function find_creator """
        self.assertEqual(find_creator("Man In Square"), "Alberto Giacometti")
        self.assertEqual(find_creator("Landscape With A Tree In The Wind"), "Vincent van Gogh")

    def test_invalid_find_creator(self):
        """ This function tests invalid input for commandline function find_creator """
        self.assertEqual(find_creator("asdfasdfadf"), None)
        self.assertRaises(TypeError, find_creator, 1)

    def test_valid_count_origin(self):
        """ This function tests valid input for commandline function origin_count """
        self.assertEqual(origin_count("France"), "The number of artists with stolen art who are from France: 10")
        self.assertEqual(origin_count("Mexico"), "The number of artists with stolen art who are from Mexico: 1")

    def test_invalid_count_origin(self):
        """ This function tests invalid input for commandline function origin_count """
        self.assertEqual(origin_count("asdfasdfadf"), None)
        self.assertRaises(TypeError, origin_count, 1)

    def test_valid_count_stolen_by_artist(self):
        """ This function tests valid input for commandline function count_stolen_by_artist """
        self.assertEqual(count_stolen_by_artist("Gustav Klimt"), 4)
        self.assertEqual(count_stolen_by_artist("Andy Warhol"), 40)

    def test_inavlid_count_stolen_by_artist(self):
        """ This function tests invalid input for commandline function count_stolen_by_artist """
        self.assertEqual(count_stolen_by_artist("Theodore Roosevelt"), 0)
        self.assertRaises(TypeError, count_stolen_by_artist, 1)



if __name__ == '__main__':
    unittest.main()
