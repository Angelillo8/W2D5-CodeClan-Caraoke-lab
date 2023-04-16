import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Alejandra Martinez", "Mr Brightside", 300)
    
    def test_guest_has_name(self):
        self.assertEqual("Alejandra Martinez", self.guest1.name)

    def test_guest_has_favourite(self):
        self.assertEqual("Mr Brightside", self.guest1.favourite_song)

    def test_guest_has_wallet(self):
        self.assertEqual(300, self.guest1.wallet)