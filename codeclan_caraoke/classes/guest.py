class Guest:
    def __init__(self, input_name, input_favourite_song, input_wallet):
        self.name = input_name
        self.favourite_song = input_favourite_song
        self.wallet = input_wallet

    def guest_pay_fee(self, amount):
        self.wallet -= amount