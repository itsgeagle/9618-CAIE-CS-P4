# Question 2 (a) - declare class Character
class Character:

    # private Name as string
    # private XCoordinate as integer
    # private YCoordinate as integer

    def __init__(self, TheName, TheXCoordinate, TheYCoordinate):
        self.Name = TheName
        self.XCoordinate = TheXCoordinate
        self.YCoordinate = TheYCoordinate

    # Question 2 (b) - write getter methods

    def GetName(self):
        return self.Name

    def GetX(self):
        return self.XCoordinate

    def GetY(self):
        return self.YCoordinate

    # Question 2 (c) - write method ChangePosition()

    def ChangePosition(self, XChange, YChange):
        self.XCoordinate += XChange
        self.YCoordinate += YChange


# Question 2 (d) - fetch data from Characters.txt
Characters = []
TextFile = "Characters.txt"
try:
    File = open(TextFile, "r")
    for i in range(10):
        Name = File.readline().strip().lower()
        XCoordinate = int(File.readline().strip())
        YCoordinate = int(File.readline().strip())
        Characters.append(Character(Name, XCoordinate, YCoordinate))
    File.close()
except FileNotFoundError:
    print("File not found")

# Question 2 (e) - write search functionality
Found = False
FoundPos = -1

while not Found:
    RequestedName = input("Enter the Character to move: ").strip("\n").lower()
    for i in range(len(Characters)):
        if Characters[i].GetName() == RequestedName:
            Found = True
            FoundPos = i
            break

# Question 2 (f) - write code to move character
Valid = False
while not Valid:
    Move = input("Which direction would you like to move the character? (A/W/S/D): ")
    if Move.upper() == "A":
        Valid = True
        Characters[FoundPos].ChangePosition(-1, 0)
    elif Move.upper() == "W":
        Valid = True
        Characters[FoundPos].ChangePosition(0, 1)
    elif Move.upper() == "S":
        Valid = True
        Characters[FoundPos].ChangePosition(0, -1)
    elif Move.upper() == "D":
        Valid = True
        Characters[FoundPos].ChangePosition(1, 0)

# Question 2 (g) (i) - write code to output confirmation message
print(f'{Characters[FoundPos].GetName()} has changed coordinates to X = {Characters[FoundPos].XCoordinate} and Y = {Characters[FoundPos].YCoordinate}')
