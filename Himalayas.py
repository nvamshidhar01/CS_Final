import textwrap as tw

class Player: #class to store player data, like inventory, location, etc.
    def __init__(self):
        self.name = ""
        self.inventory = []
        self.loc = "sign"


class Room:
    def __init__(self, name):
        self.name = name
        self.filepath = name + ".txt"
        self.objects = []
        self.locations = []
        self.initialDescription = ""
        self.normalDescription = ""
        self.visited = False
        self.assignDefaults()

    def assignDefaults(self):
        #read default file into a list of each line
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
        self.normalDescription = (self.normalDescription).rstrip("\n") #remove whitespace on last line
        n+=1
        while raw[n] != "OBJECTS": # set list of locations available
            temp = []
            temp = raw[n].split(":")
            self.locations.append(temp)
            n+=1
        n+=1
        for i in (raw[n:]): #set list of objects (formatted as a list of lists containing an object and description)
            temp = []
            temp = i.split(":")
            self.objects.append(temp)         #read defaults from room file

    def printInitial(self):
            print(self.title)
            print(tw.fill(self.initialDescription, width=50))
            self.visited = True

    def roomDescription(self):
        objstr = "There is a "
        print(self.title)
        print(tw.fill(self.normalDescription, width=50))
        for i in self.objects:
            if self.objects.index(i) != len(self.objects)-1:
                objstr = objstr + i[0] + ", "
            else:
                objstr = objstr + "and " + i[0] + " in here."
        if len(self.objects) > 0 :
            print(tw.fill(objstr, width=50))

def goTo(room, player, ): #function to instantiate/change rooms

    try:
        player.loc = room.name
        room.roomDescription()
    except:
        print("You cant go there")

def main():
    player1 = Player()
    rooms = {
    "yakshack":Room("yakshack"),
    "sign" : Room("sign"),
    "river" : Room("river"),
    "souvenir" : Room("souvenir"),
    "lodge" : Room("lodge"),
    "well" : Room("well")
    }
    #rooms["yakshack"].title = "changed"
    #print(rooms["yakshack"].title)
    sign = Room("sign")
    river = Room("river")
    souvenir = Room("souvenir")
    lodge = Room("lodge")
    well = Room("well")
    #yakshack = Room("yakshack")
    goTo(rooms["river"], player1)
    #print(rooms[player1.loc].filepath)
    goTo(rooms["sign"], player1)
    print(player1.loc)
main()
