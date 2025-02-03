class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self, address):
        self.address = address
        self.rooms = [Room("Living Room"), Room("Bedroom"), Room("Kitchen")]

house = House("Chembukkavu, Thrissur - 680020 Kerala")

for room in house.rooms:
    print(room.name)

