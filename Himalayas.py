
""" OLDER VERSION: IGNORE - FOR REFERENCE
room_defaults = []
room_d = open("room_defaults.txt", "r")
raw = room_d.readlines() #read each line into an array
roomNums = len(raw) #counter for total number of rooms read in
for line in raw: #creates a list of lists for each room containing default objects, available locations, etc.
    line = line.rstrip("\n")
    room_defaults.append(line.split(","))
room_d.close()
"""
def goTo(room): #function to instantiate/change rooms
    pass #use try except to catch room load errors

class Player: #class to store player data, like inventory, location, etc.
    def __init__(self):
        self.name = ""
        self.inventory = []


class Room:
    def __init__(self, name):
        boundary = ["INITIAL","NORMAL","LOCATIONS","OBJECTS"]
        self.name = name
        self.filepath = name + ".txt"
        #separate room default values file into class attributes
        file = open(self.filepath, "r")
        raw = file.readlines()
        final = []
        for line in raw:
            line = line.rstrip("\n")
            final.append(line)

        print(final)

        ''' OLDER VERSION - IGNORE - FOR REFERENCE
        #dictionary containing naming and default values for each room
        dValues = {
        "signroom" : room_defaults[0],
        "river" : room_defaults[1],
        "souvenir" : room_defaults[2],
        "lodge" : room_defaults[3],
        "well" : room_defaults[4],
        "yakshack" : room_defaults[5]
        }
        #print(dValues[self.name])
        self.defaults = dValues[self.name]
        self.objects = []
        self.locations = []

        #while loop to sort defaults into object lists
        n = 0
        counter = self.defaults[n]
        while(counter != "locations"):
            self.objects.append(self.defaults[n])
            n += 1
            counter = self.defaults[n]
        n+=1
        #for loop to sort defaults into locations
        for i in range(n,len(self.defaults)):
            self.locations.append(self.defaults[n])
        '''
    def roomDescription(self, player):         #print out room description
        for n in range(len(self.objects)):
            if not any(self.objects[n] in s for s in player.inventory):
                print(self.objects[n])

def main():
    player1 = Player()
    signroom = Room("signroom")
    river = Room("river")

main()
