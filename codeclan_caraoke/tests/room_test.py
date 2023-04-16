import unittest
from classes.song import Song
from classes.guest import Guest
from classes.room import Room

class TestRoom (unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("That's Alright", "Elvis Presley")
        self.song_2 = Song("Hakuna Matata", "The Lion King")
        self.song_3 = Song("A Whole New World", "Aladdin soundtrack")

        self.guest_1 = Guest("Alejandra Martinez", "Mr Brightside", 350)
        self.guest_2 = Guest("Hugo Elvira", "Paranoid", 100)
        self.guest_3 = Guest("Victor Batista", "Abrázame Muy Fuerte", 220)

        self.room_1 = Room("Room I", 5)

    def test_room_has_name(self):
        self.assertEqual("Room I", self.room_1.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room_1.capacity)
    
    def test_room_add_songs(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.songs_list))
        self.room_1.add_song([self.song_2, self.song_3])
        self.assertEqual(3, len(self.room_1.songs_list))

    def test_check_in_guests(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))
        self.room_1.check_in_guest(self.guest_2)
        self.assertEqual(2, len(self.room_1.guests))
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(3, len(self.room_1.guests))
    
    def test_check_out_guests(self):
        self.room_1.check_in_guest([self.guest_1, self.guest_2, self.guest_3])
        self.room_1.check_out_guests()
        self.assertEqual(0, len(self.room_1.guests))
    
    def test_add_songs_with_song_generator(self):
        song2 = Song("Dancing Queen", "ABBA")
        self.room_1.add_song(song2)
        self.assertEqual(1, len(self.room_1.songs_list))
        self.room_1.add_song(self.room_1.generate_songs(7))
        self.assertEqual(8, len(self.room_1.songs_list))

    