from other.generators import *

class Room:
    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.songs_list = []
        self.guests = []

    def add_song(self, song):
        if type(song) == list:
            self.songs_list += song
        else:
            self.songs_list.append(song)

    def check_in_guest(self, guest_to_check_in):
        self.guests.append(guest_to_check_in)
    
    def check_out_guests(self):
        self.guests.clear()

    def generate_songs(self, number_of_times):
        new_songs = song_generator(number_of_times)
        return (new_songs)
    
    def room_is_full(self):
        room_is_full = False
        if len(self.guests) == self.capacity:
            room_is_full = True
        return room_is_full
