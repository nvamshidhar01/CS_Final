
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
        self.name = name
        self.filepath = name + ".txt"
        self.objects = []
        self.locations = []
        self.initialDescription = ""
        self.normalDescription = ""
        #read defaults from room file
        file = open(self.filepath, "r")
        raw = []
        for line in file:
            line = line.rstrip("\n")
            raw.append(line)
        file.close()

        self.title = raw[0]
        # set of while and for loops to sort default room data into appropriate attributes, allows for varied numbers of locations and objects
        n = 2
        while raw[n] != "NORMAL": #set initial description attribute, should copy exactly what you put in INITIAL area in the txt file
            self.initialDescription = self.initialDescription + str(raw[n]) + "\n"
            n += 1
        n+=1
        while raw[n] != "LOCATIONS": #set normal description attribute, should copy exactly what you put in NORMAL area in the txt file
            self.normalDescription = self.normalDescription + str(raw[n]) + "\n"
            n+=1
        n+=1
        while raw[n] != "OBJECTS": # set list of locations available
            self.locations.append(raw[n])
            n+=1
        n+=1
        for i in (raw[n:]): #set list of objects (formatted as a list of lists containing an object and description)
            temp = []
            temp = i.split(":")
            self.objects.append(temp)



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
    def roomDescription(self, player):
        avItems = [] #empties list of available items in the room
        objstr = "There is a "
        print(self.normalDescription)
        for i in self.objects:
            if self.objects.index(i) != len(self.objects)-1:
                objstr = objstr + i[0] + ", "
            else:
                objstr = objstr + "and " + i[0] + " in here."
        if len(self.objects) > 0 :
            print(objstr)


def main():
    player1 = Player()
    signroom = Room("signroom")
    river = Room("river")
    '''
    print(signroom.title)
    print(signroom.initialDescription)
    print(signroom.normalDescription)
    print(signroom.locations)
    print(signroom.objects)
    '''
    signroom.roomDescription(player1)
main()
