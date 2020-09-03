# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player, room):
        self.player = player
        self.room = room
    
    inventory = []

    def check_for_items(self):
        if not self.room.items:
            print('You see no items in this room')
        else:
            print(f'You see the following items:')
            for item in self.room.items:
                print(item)

    def take_item(self, item):
        act = input('Do you want to take all items? y or n: ')
