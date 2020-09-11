from colorama import Fore, Style


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'\n{Fore.GREEN}You have picked up {self.name}!{Style.RESET_ALL}\n')

    def on_drop(self):
        print(f'\n{Fore.YELLOW}You have dropped {self.name}!{Style.RESET_ALL}\n')

    def add_to_room(self, room):
        room.items.append(self)
        return room.items

    def remove_from_room(self, room):
        room.items.remove(self)
        return room.items

    def add_to_player(self, player):
        player.inventory.append(self)
        self.remove_from_room(player.current_room)
        self.on_take()
        player.print_inventory()

    def remove_from_player(self, player):
        player.inventory.remove(self)
        self.add_to_room(player.current_room)
        self.on_drop()
        player.print_inventory()
