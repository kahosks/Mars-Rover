import sys
import csv


class Rover:
    def __init__(self, x, y, dir, inst):
        self.x = x
        self.y = y
        self.dir = dir
        self.inst = inst

    def forward(self):
        print("Advance!")
        if self.dir == "N":
            self.y += 1
        elif self.dir == "E":
            self.x += 1
        elif self.dir == "S":
            self.y -= 1
        elif self.dir == "W":
            self.x -= 1
        for x in Fleet:
            if x != self and x.x == self.x and x.y == self.y:
                raise Exception("Faulty Instructions: Collision imminent!!")

    def turn_left(self):
        print("Turn Left")
        if self.dir == "N":
            self.dir = "W"
        elif self.dir == "E":
            self.dir = "N"
        elif self.dir == "S":
            self.dir = "E"
        elif self.dir == "W":
            self.dir = "S"

    def turn_right(self):
        print("Turn Right")
        if self.dir == "N":
            self.dir = "E"
        elif self.dir == "E":
            self.dir = "S"
        elif self.dir == "S":
            self.dir = "W"
        elif self.dir == "W":
            self.dir = "N"

    def initiate(self):
        self.report()
        for i in self.inst:
            if i == "M":
                self.forward()
            elif i == "L":
                self.turn_left()
            elif i == "R":
                self.turn_right()
            self.report()
        print("Scanning done.")

    def report(self):
        print(self.x, self.y, self.dir)
        if self.x > MAX_X or self.x < 0 or self.y > MAX_Y or self.y < 0:
            print("WARNING: This Rover has moved beyond bounds!!")

#MAX_X = ""
#MAX_Y = ""
#Fleet = []
#r1 = Rover(1,2,'N','LMLMLMLMM')
#r2 = Rover(3,3,'E','MMRMMRMRRM')
#Fleet.append(r1)
#Fleet.append(r2)


if __name__ == '__main__':

    #Uses csv module
    Fleet = []

    with open (sys.argv[1]) if len(sys.argv) >= 3 else open ("inputcsv.txt") as file:
        reader = csv.reader(file, delimiter=",")
        line_iter = 0
        for line in reader:
            if line_iter == 0:
                print(line)
                MAX_X = int(line[0])
                MAX_Y = int(line[1])
                line_iter += 1
            else:
                print(line)
                Fleet.append(Rover(int(line[0]), int(line[1]), line[2], next(reader)))

    #Without csv module
    # input = open(sys.argv[1]) if len(sys.argv) >= 3 else open("inputcsv.txt")
    # l = input.readline()
    #MAX_X = int(l.split(",")[0])
    #MAX_Y = int(l.split(",")[1])
    print("Max Coordinates: " + str(MAX_X) + "," + str(MAX_Y))

    #WIthout List comprehension
    #for line in input:
        #print ("Input: " + line)
        #if len(line.split(",")) == 2:
        #    MAX_X = int(line.split(",")[0])
        #    MAX_Y = int(line.split(",")[1])
        #    print("Max Coordinates: " + str(MAX_X) + "," + str(MAX_Y))
        #elif len(line.split(",")) == 3:
        #    x = int(line.split(",")[0])
        #    y = int(line.split(",")[1])
        #    dir = line.split(",")[2].strip()
        #    print("New Rover: " + str(x) + "," + str(y) + "," + dir)
        #    inst = next(input).replace(",", "").strip()
        #    Fleet.append(Rover(x, y, dir, inst))

    #With List comprehension
    #Fleet = [Rover(int(splitline[0]), int(splitline[1]), splitline[2].strip(), next(input).replace(",", "").strip()) for splitline in (line.split(",") for line in input)]

    print("Rovers in the Fleet:")
    for r in Fleet:
        r.report()

    for r in Fleet:
        print(r)
        r.initiate()

    print("Final Locations:")
    for r in Fleet:
        r.report()
