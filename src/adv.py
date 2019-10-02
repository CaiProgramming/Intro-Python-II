from player import Player
from room import Room

import random
import os
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons","outside"
                     ,["         / /","        /  \ "," ______/    \______",
                     "|                  |","|                  |",
                     "|                  |","|                  |",
                     "|__________________|"
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""",'foyer',
                [' ______| |_________',
                '|                __  ','|               |',
                '|	________|','|      |',
                "|_  ___|"," / / ","/  \ "]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                'overlook',
                ['_________♀__________',"####################",
                "#### ________#######","####|        |######",
                "####|       /#######","#####\     /########",
                "######\   /#########","_______| |__________"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",'narrow',
                ['   /  / ','  /  / ','  |  |','  |  |','  |  |','__|  |','_____| ']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                'treasure',
                [' __________________','|                § |',
                '|    § §      §    |','|      §   §       |',
                '|                  |','|     §    §       |',
                '|______      ____§_|','       |    |']),
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
pName = input('Character\'s name: ')
pSex = input('Character\'s sex: ')
pAge = input('Character\'s age: ')

char = Player(pName,pSex,pAge,"outside");

exit = 0;
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
print('you\'re movement is W/A/S/D ',end='\n\n')
print('W=North A=West S=South D=East',end='\n\n')
print('"q", quit the game.',end='\n\n')

while not exit:
    randomNum = random.randint(1,101)
    print(room[char.currentRoom()].roomName(), end='\n\n')
    print(room[char.currentRoom()].roomDesc(), end='\n\n')
    for i in room[char.currentRoom()].roomMap():
        print(i)
    movement = input('Where would you like to go : ')
    if movement.lower() == 'q':
        exit = 1;
    if movement.lower() == 'w':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].n_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
    if movement.lower() == 'a':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].w_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
    if movement.lower() == 's':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].s_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
    if movement.lower() == 'd':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].e_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
