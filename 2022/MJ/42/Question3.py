# Question 3 (d) pt 1
global NumbersChosen

# Question 3 (a) - write class Card and constructor
class Card:

    # Number as integer
    # Colour as string

    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour

    # Question 3 (b) - write getter methods
    def getNumber(self):
        return self.__Number

    def getColour(self):
        return self.__Colour


# Question 3 (d) pt 2
def chooseCard():
    global NumbersChosen
    flagContinue = True
    while flagContinue:
        CardSelected = int(input("Select a card number: "))
        if CardSelected < 1 or CardSelected > 30:
            print("Please select a card number between 1 and 30.")
        elif NumbersChosen[CardSelected - 1]:
            print("Already taken")
        else:
            print("Valid")
            flagContinue = False
    NumbersChosen[CardSelected - 1] = True
    return CardSelected - 1


# Question 3 (c) - declare and initialize Card
CardArray = [0 for i in range(30)]  # integer

try:
    file = open('CardValues.txt', 'r')
    for x in range(0, 30):
        number = int(file.readline().strip('\n'))
        colour = file.readline().strip('\n')
        CardArray[x] = Card(number, colour)
    file.close()
except IOError:
    print('File not found')

NumbersChosen = [False for i in range(30)]

# Question 3 (e) (i) -
Player1 = []
for x in range(0, 4):
    ReturnNumber = chooseCard()
    Player1.append(CardArray[ReturnNumber])
for x in range(0, 4):
    print(Player1[x].getNumber())
    print(Player1[x].getColour())
