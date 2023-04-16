import unittest
from classes.song import Song
from classes.guest import Guest
from classes.room import Room
from classes.caraoke import Caraoke

class TestCaraoke(unittest.TestCase):
    def setUp(self):
        self.caraoke = Caraoke("Karaoke Krema", 550, 15)
        self.rooms = [Room("Room I", 5), Room("Room II", 8)]
        self.caraoke.add_room(self.rooms)

    def test_caraoke_has_name(self):
        self.assertEqual("Karaoke Krema", self.caraoke.name)
    
    def test_caraoke_has_till(self):
        self.assertEqual(550, self.caraoke.till)
    
    def test_add_new_guests_to_queue(self):
        guest_1 = Guest("Alejandra Martinez", "Mr Brightside", 300)
        self.caraoke.add_new_guests_to_queue(guest_1)
        self.assertEqual(1, len(self.caraoke.guests_queue))
        guest_2 = Guest("Hugo Elvira", "Paranoid", 100)
        self.caraoke.add_new_guests_to_queue(guest_2)
        self.assertEqual(2, len(self.caraoke.guests_queue))
        self.caraoke.add_new_guests_to_queue(self.caraoke.generate_guests(7))
        self.assertEqual(9, len(self.caraoke.guests_queue))

    def test_collec_fee(self):
        guest_1 = Guest("Alejandra Martinez", "Mr Brightside", 300)
        self.caraoke.collect_fee(guest_1)
        self.assertEqual(285, guest_1.wallet)
        self.assertEqual(565, self.caraoke.till)

    def test_checking_in_guests(self):
        self.caraoke.add_new_guests_to_queue(self.caraoke.generate_guests(5))
        self.assertEqual(0, len(self.caraoke.rooms[0].guests))
        self.assertEqual(5, len(self.caraoke.guests_queue))
        self.caraoke.checking_in_guests(self.caraoke.guests_queue, self.caraoke.rooms[0])
        self.assertEqual(0, len(self.caraoke.guests_queue))
        self.assertEqual(5, len(self.caraoke.rooms[0].guests))
        self.assertEqual(625, self.caraoke.till)

    def test_checking_in_guests(self):
        self.caraoke.add_new_guests_to_queue(self.caraoke.generate_guests(5))
        self.assertEqual(0, len(self.caraoke.rooms[0].guests))
        self.assertEqual(5, len(self.caraoke.guests_queue))
        self.caraoke.checking_in_guests(self.caraoke.guests_queue, self.caraoke.rooms[0])
        self.assertEqual(0, len(self.caraoke.guests_queue))
        self.assertEqual(5, len(self.caraoke.rooms[0].guests))
        self.assertEqual(625, self.caraoke.till)
    
    def test_checking_in_guests_room_is_full(self):
        self.caraoke.add_new_guests_to_queue(self.caraoke.generate_guests(6))
        self.assertEqual(0, len(self.caraoke.rooms[0].guests))
        self.assertEqual(6, len(self.caraoke.guests_queue))
        self.caraoke.checking_in_guests(self.caraoke.guests_queue, self.caraoke.rooms[0])
        self.assertEqual(5, len(self.caraoke.rooms[0].guests))
        self.assertEqual(1, len(self.caraoke.guests_queue))
        self.assertEqual("Please wait until the room is empty or try another room.",self.caraoke.checking_in_guests(self.caraoke.guests_queue, self.caraoke.rooms[0]))