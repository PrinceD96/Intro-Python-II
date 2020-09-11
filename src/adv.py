from room import Room
from player import Player
from item import Item
import random
from os import system, name
from colorama import Fore, Style

# Declare the items

sword = Item("sword", "This weapon makes you powerful")
shield = Item("shield", "Gives you the most protection")
axe = Item("axe", "Heavy but dangerous")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [sword, shield]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [axe, sword]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [shield]),
    'dome':     Room("Dome", """There's only a way in, you can't escape from this room.""", [sword, shield])
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
room["treasure"].n_to = room["dome"]
room["dome"].s_to = room["treasure"]

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
    f"\nWelcome to the Adventure Game, {player1.name}!\n\nYou have been randomly placed in room {player1.current_room.name}\n\n{Fore.CYAN}Type 'h' or 'help' to read the instructions{Style.RESET_ALL}"
)

instructions = "".join(
    (
        f"\n\n{Fore.CYAN}INSTRUCTIONS: \n\n",
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
        print(f"\nGoodbye, {player1.name}!\n")
        is_playing = False
        break

    if cmd == "help" or cmd == "h":
        clear_terminal()
        print(instructions)

    elif cmd == "i" or cmd == "inventory":
        clear_terminal()
        player1.print_inventory()

    else:
        cmd = cmd.split(' ')
        if len(cmd) == 1:
            clear_terminal()
            player1.move(cmd[0])

        elif len(cmd) == 2:
            # clear_terminal()

            if cmd[0] == 'get' or cmd[0] == 'take':
                item_to_take = cmd[1]

                for item in player1.current_room.items:
                    if item.name == item_to_take:
                        item_to_take = item
                        item_to_take.add_to_player(player1)
                        break

                else:
                    print(
                        f'\n{Fore.RED}{item_to_take} is not available in this room!{Style.RESET_ALL}')

            elif cmd[0] == 'drop':
                item_to_drop = cmd[1]

                for item in player1.inventory:
                    if item.name == item_to_drop:
                        item_to_drop = item
                        item_to_drop.remove_from_player(player1)
                        break

                else:
                    print(
                        f"{Fore.RED}You can't drop {item_to_drop} because it's not in your inventory!{Style.RESET_ALL}")


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
