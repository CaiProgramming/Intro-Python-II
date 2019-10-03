from player import Player
from room import Room
from potion import Potion
from weapon import Weapon
import random
import os
#declare all weapons
potion0 = Potion("Health potion",3.5,"Adds health to your character","Restoration",'potion');
weapon0 = Weapon("Broken Sword",1,"Broken sword from a failed blacksmith",-1,'weapon');
potion1 = Potion("Mana potion",3,"Adds mana to your character","Restoration",'potion');
weapon1 = Weapon("Necromancers Staff",15,"Staff containing horrible memories",50,'weapon');
potion2 = Potion("Posion potion",2,"Deals damage to enemies","DOT",'potion');
weapon2 = Weapon("Tattered book",5,"Contains magic spells",10,'weapon');
potion3 = Potion("Stamina potion",2,"Adds stamina to your character","Restoration",'potion');
weapon3 = Weapon("Mighty Hammer",25,"Hammer made by dwarves in your backyard",125,'weapon');
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons","outside"
                     ,["         / /","        /  \ "," ______/    \______",
                     "|                  |","|                  |",
                     "|                  |","|                  |",
                     "|__________________|"
                     ],[potion0,potion1]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""",'foyer',
                [' ______| |_________',
                '|                __  ','|               |',
                '|	________|','|      |',
                "|_  ___|"," / / ","/  \ "],[weapon0]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                'overlook',
                ['_________♀__________',"####################",
                "#### ________#######","####|        |######",
                "####|       /#######","#####\     /########",
                "######\   /#########","_______| |__________"],[weapon2,weapon1]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",'narrow',
                ['   /  / ','  /  / ','  |  |','  |  |','  |  |','__|  |','_____| '],[potion2]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                'treasure',
                [' __________________','|                § |',
                '|    § §      §    |','|      §   §       |',
                '|                  |','|     §    §       |',
                '|______      ____§_|','       |    |'],[weapon3]),
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


while not exit:
    print('you\'re movement is W/A/S/D ',end='\n\n')
    print('W=North A=West S=South D=East',end='\n\n')
    print('"q", quit the game.',end='\n\n')
    print('"e", search room.',end='\n\n')
    print('"i", show inventory.',end='\n\n')
    #random damage number
    randomNum = random.randint(1,101)
    #print room name and description
    print(room[char.currentRoom()].roomName(), end='\n\n')
    print(room[char.currentRoom()].roomDesc(), end='\n\n')
    #render map for room
    for i in room[char.currentRoom()].roomMap():
        print(i)
    #player input
    movement = input('Where would you like to go : ')
    if movement.lower() == 'q':
        exit = 1;
    #search room
    if movement.lower() == 'e':
        os.system('cls||clear')
        #check if items have been picked up
        done = 0
        if room[char.currentRoom()].roomItems():
            while not done:
                print('press "o" to exit item pick up',end='\n\n')
                #print all items in room
                for x in room[char.currentRoom()].roomItems():
                    print('item in room:', x.itemName(),end='\n\n')
                pickup = input('What item would you like to pickup [get] [item] : ')
                #any item picked up?
                pickedup = 0
                for x in room[char.currentRoom()].roomItems():
                    pickSplit = pickup.split(' ')
                    pickSplitItem = " ".join(pickSplit[1:])
                    #add item to inventory
                    if pickSplit[0].lower() == 'get':
                        if pickSplitItem.lower() == x.itemName().lower():
                            pickedup = 1
                            os.system('cls||clear')
                            print('added to your inventory',x.itemName(),x.itemDesc())
                            char.addItems(x)
                            room[char.currentRoom()].removeItem(x)
                    elif not pickSplit[0].lower() == 'o':
                        os.system('cls||clear')
                        print('please use [get] [item] syntax',end='\n\n')
                        break
                #exit
                if pickup.lower() == 'o':
                    done = 1
                    os.system('cls||clear')
                if not room[char.currentRoom()].roomItems():
                    done = 1
                    os.system('cls||clear')
                if not pickedup and not done:
                    print('item name doesnt exists',end='\n\n')

        else:
            #if room is empty tell the player
            print('room is empty')
    #check inventory
    if movement.lower() == 'i':
        os.system('cls||clear')
        #get player items
        if char.playerItems():
            done = 0
            while not done:
                action = input('press e to look at inventory, press d to drop items in inventory : ')
                if action.lower() == 'e':
                    done = 1
                    for x in char.playerItems():
                    #check item type for output
                        if x.itemType() == 'weapon':
                            print('item in your inventory','name:',x.itemName(),
                            'desc:',x.itemDesc(),"damage:",x.itemDamage())
                        if x.itemType() == 'potion':
                            print('item in your inventory','name:',x.itemName(),
                            'desc:',x.itemDesc(),"effect:",x.itemEffect())
                #go to drop menu
                if action.lower() == 'd':
                    while not done:
                        #list items in inventory
                        for x in char.playerItems():
                            print('item in inventory:', x.itemName(),end='\n\n')
                        print("press 'o' to exit inventory dropping",end='\n\n')
                        action = input('What item would you like to drop [drop] [item] : ')
                        dropped = 0
                        print(action)
                        #if o exit
                        if not action.lower() == 'o':
                            #get items
                            for x in char.playerItems():
                                dropSplit = action.split(' ')
                                dropSplitItem = " ".join(dropSplit[1:])
                                #drop item from inventory
                                if dropSplit[0].lower() == 'drop':
                                    print(dropSplitItem.lower())
                                    print(x.itemName().lower())
                                    if dropSplitItem.lower() == x.itemName().lower():
                                        dropped = 1
                                        os.system('cls||clear')
                                        print('dropped from your inventory',x.itemName(),x.itemDesc())
                                        char.dropItem(x)
                                #incorrect syntax
                                else:
                                    os.system('cls||clear')
                                    print('please use [drop] [item] syntax',end='\n\n')
                                    break
                        if action.lower() == 'o':
                            done = 1
                            os.system('cls||clear')
                        if not dropped and not done:
                            os.system('cls||clear')
                            print('item name doesnt exists',end='\n\n')

        else:
            #if inv empty tell the player
            print('inventory empty')

    '''
    movement go north
    '''
    if movement.lower() == 'w':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].n_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
    '''
    movement go west
    '''
    if movement.lower() == 'a':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].w_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
    '''
    movement go south
    '''
    if movement.lower() == 's':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].s_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
    '''
    movement go east
    '''
    if movement.lower() == 'd':
        os.system('cls||clear')
        try:
            char.changeRoom(room[char.currentRoom()].e_to.roomId())
        except:
            print('You hit your face against a wall and take',str(randomNum),'damage',end='\n\n')
