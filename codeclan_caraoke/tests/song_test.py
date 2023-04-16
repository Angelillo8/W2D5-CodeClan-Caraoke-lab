import unittest
from classes.song import Song
# from other.generators import song_generator

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song2 = Song("Dancing Queen", "ABBA")

    def test_song_has_name(self):
        self.assertEqual("Dancing Queen", self.song2.name)

    def test_song_has_artist(self):
        self.assertEqual("ABBA", self.song2.artist)
