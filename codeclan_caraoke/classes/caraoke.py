from other.generators import *

class Caraoke:
    def __init__(self, input_name, input_till, input_fee):
        self.name = input_name
        self.till = input_till
        self.fee = input_fee
        self.rooms = []
        self.guests_queue = []

    def add_room(self, room):
        if type(room) == list:
            self.rooms += room
        else:
            self.rooms.append(room)

    def add_new_guests_to_queue(self, guest):
        if type(guest) == list:
            self.guests_queue.extend(guest)
        else:
            self.guests_queue.append(guest)

    def remove_guest_from_queue(self, guest):
        self.guests_queue.remove(guest)

    def generate_guests(self, number_of_times):
        new_guests = guest_generator(number_of_times)
        return new_guests

    def collect_fee(self, guest):
        guest.guest_pay_fee(self.fee)
        self.till += self.fee

    def checking_in_guests(self, guests_to_check_in, room):
        if type(guests_to_check_in) == list:
            for guest in guests_to_check_in:
                if room.room_is_full() == False:
                    self.collect_fee(guest)
                    room.check_in_guest(guest)
            for guest in room.guests:
                if guest in guests_to_check_in:
                    self.remove_guest_from_queue(guest)
        else:
            if room.room_is_full() == False:
                self.collect_fee(guests_to_check_in)
                room.check_in_guest(guests_to_check_in)
                self.remove_guest_from_queue(guests_to_check_in)
        if room.room_is_full() == True and self.guests_queue != 0:
            return "Please wait until the room is empty or try another room."
                

    
