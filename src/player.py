# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Back, Style


class Player:
    def __init__(self, name, initial_room):
        self.name = name
        self.current_room = initial_room

    def __repr__(self):
        return f"My name is {self.name} and I'm currently in room {self.current_room.name}."

    def move(self, direction):
        def no_room():
            print(f'{Fore.RED}Only darkness awaits there!{Style.RESET_ALL}')

        def print_current_room():
            print(
                f'{Fore.GREEN}You are now in room {self.current_room.name}:\n\n{self.current_room.description}{Style.RESET_ALL}')

        if direction.lower() == 'n':
            if self.current_room.n_to:
                self.current_room = self.current_room.n_to
                print_current_room()
            else:
                no_room()
        if direction.lower() == 's':
            if self.current_room.s_to:
                self.current_room = self.current_room.s_to
                print_current_room()
            else:
                no_room()
        if direction.lower() == 'e':
            if self.current_room.e_to:
                self.current_room = self.current_room.e_to
                print_current_room()
            else:
                no_room()
        if direction.lower() == 'w':
            if self.current_room.w_to:
                self.current_room = self.current_room.w_to
                print_current_room()
            else:
                no_room()
