import unittest
from ProductionCode.command_line import *

class TestCommandLines(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_creator(self):
        self.assertEqual(find_creator("Man In Square"), "Alberto Giacometti")
        self.assertEqual(find_creator("Landscape With A Tree In The Wind"), "Vincent van Gogh")

        self.assertEqual(find_creator("asdfasdfadf"), None)
        self.assertRaises(TypeError, find_creator, 1)

    def test_find_artwork(self):
        self.assertEqual(find_artwork("René Magritte"), ["Les Bijoux Indiscrets", "Moments Inoubliables Du Cinema", "Bust Of A Soldier", "Morning Promises"])

        self.assertEqual(find_artwork("asdfasdfadf"), [])
        self.assertRaises(TypeError, find_artwork, 1)

    def test_count_origin(self):
        self.assertEqual(origin_count("France"), "The number of artists with stolen art who are from France: 10")
        self.assertEqual(origin_count("Mexico"), "The number of artists with stolen art who are from Mexico: 1")

        self.assertEqual(origin_count("asdfasdfadf"), None)
        self.assertRaises(TypeError, origin_count, 1)

    def test_count_stolen_by_artist(self):
        self.assertEqual(count_stolen_by_artist("Gustav Klimt"), 4)
        self.assertEqual(count_stolen_by_artist("Andy Warhol"), 40)

        self.assertEqual(count_stolen_by_artist("Theodore Roosevelt"), 0)
        self.assertRaises(TypeError, count_stolen_by_artist, 1)



if __name__ == '__main__':
    unittest.main()
