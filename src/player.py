# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Style


class Player:
    def __init__(self, name, initial_room, items=None):
        self.name = name
        self.current_room = initial_room
        if items == None:
            self.inventory = []
        else:
            self.inventory = items

    def __repr__(self):
        return f"My name is {self.name} and I'm currently in room {self.current_room.name}."

    def print_inventory(self):
        if len(self.inventory) == 0:
            inventory = 'no items'
        else:
            inventory = ', '.join([item.name for item in self.inventory])
        print(f'You have {inventory} in your inventory!')

    def print_current_room(self):
        if len(self.current_room.items) == 0:
            items_list = 'None'
        else:
            items_list = ', '.join(
                [item.name for item in self.current_room.items])
        print(
            f'{Fore.GREEN}You have moved to room\n\n{Fore.WHITE}{self.current_room.name}: \n\n{self.current_room.description}\n\n{Fore.CYAN}Items available: {items_list}{Style.RESET_ALL}')

    def move(self, direction):
        def no_room():
            print(f'{Fore.RED}Only darkness awaits there!{Style.RESET_ALL}')

        if direction.lower() == 'n':
            if self.current_room.n_to:
                self.current_room = self.current_room.n_to
                self.print_current_room()
            else:
                no_room()
        elif direction.lower() == 's':
            if self.current_room.s_to:
                self.current_room = self.current_room.s_to
                self.print_current_room()
            else:
                no_room()
        elif direction.lower() == 'e':
            if self.current_room.e_to:
                self.current_room = self.current_room.e_to
                self.print_current_room()
            else:
                no_room()
        elif direction.lower() == 'w':
            if self.current_room.w_to:
                self.current_room = self.current_room.w_to
                self.print_current_room()
            else:
                no_room()
        else:
            print(f'{Fore.RED}Oops... Command not valid.\n\n{Style.RESET_ALL}{Fore.CYAN}Type "h" or "help" for available commands{Style.RESET_ALL}')
