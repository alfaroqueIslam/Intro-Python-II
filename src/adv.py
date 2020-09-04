from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('Rock', 'regular rock'), 
                     Item('Worn dagger', 'An overused dagger')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('player', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
n = 1

while n == 1:
    print(player.room)
    player.check_for_items()
    p = input('Do you wish to take an item? y or n: ')
    if p == 'y':
        p1 = input('Choose item(s) separated by comma: ').split(',')
        player.get(p1)
        print('Your inventory: ')
        for item in player.inventory:
            print(item)
    p2 = input('Do you wish to drop an item? y or n: ')
    if p2 == 'y':
        p1 = input('Choose item(s) separated by comma: ').split(',')
        player.drop(p1)
        print('Your inventory: ')
        for item in player.inventory:
            print(item)
    d = input('Enter direction n for north, s for south, e for east, w for west or q to quit: ')
    s = [k for k,v in room.items() if v == player.room]
    try:
        if d == 'n':
            player.room = room[s[0]].n_to
            n = 1
        elif d == 's':
            player.room = room[s[0]].s_to
            n = 1
        elif d == 'e':
            player.room = room[s[0]].e_to
            n = 1
        elif d == 'w':
            player.room = room[s[0]].w_to
            n = 1
        elif d == 'q':
            break
        else:
            print('That is not a correct value for this room, try again')
            n = 1
    except AttributeError:
        print('That is not a correct value for this room, try again')
        n = 1

