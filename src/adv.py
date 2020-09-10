from room import Room
from player import Player
import random
from os import system, name
from colorama import Fore, Back, Style

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Clear the terminal for better readability


def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# Select a random room
initial_room = random.choice(list(room.values()))
clear_terminal()

# Get the user's name and create a player with it and place them at the initial room
name = input("\nHello there human!\n\nPlease enter your name: ")
player1 = Player(name, initial_room)

clear_terminal()
print(
    f"\nWelcome to the Adventure Game, {player1.name}!\n\nYou have been randomly placed in room {player1.current_room.name}\nType 'h' or 'help' to read the instructions"
)

instructions = "".join(
    (
        "\n\nINSTRUCTIONS: \n\n",
        "Press 'n' to go North, 'e' to go East, 's' to go South, or 'w' to go West!\n",
        "To take an item, type 'take [item_name]' or 'get [item_name]'\n",
        "To drop an item, type 'drop [item_name]'\n",
        "To check your inventory, type 'i' or 'inventory'\n"
        "To quit press 'q'\n\n",
    )
)

is_playing = True
while is_playing:
    cmd = input('> ')
    if cmd == "q":
        print(f"\nGoodbye, {player1.name}!")
        # is_playing = False
    if cmd == "help" or cmd == "h":
        clear_terminal()
        print(instructions)

    else:
        clear_terminal()
        player1.move(cmd)
        # print(f"Oops... Command not valid. Press 'h' to read instructions!")


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
