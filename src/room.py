# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description, items=None, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        if items == None:
            self.items = []
        else:
            self.items = items

    def print_room(self):
        wrapper = textwrap.TextWrapper(width=80)
        description = wrapper.wrap(text=self.description)
        for s in description:
            print(s)
        print("\n")

    def __repr__(self):
        return f"This is room {self.name}: {self.description}"
