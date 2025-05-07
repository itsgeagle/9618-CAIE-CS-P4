# Question 2 (a) - declare class Balloon and constructor
class Balloon:

    # Health as string
    # Colour as string
    # DefenceItem as string

    def __init__(self, Colour, DefenceItem):
        self.__Health = 100
        self.__Colour = Colour
        self.__DefenceItem = DefenceItem

    # Question 2 (b) - write method GetDefenceItem()
    def GetDefenceItem(self):
        return self.__DefenceItem

    # Question 2 (c) - write method ChangeHealth()
    def ChangeHealth(self, Change):
        self.__Health += Change

    # Question 2 (d) - write method CheckHealth()
    def CheckHealth(self):
        return self.__Health <= 0


# Question 2 (e) = write main program
userItem = input("Enter a defence item: ")
userColor = input("Enter a color: ")
Balloon1 = Balloon(userColor, userItem)


# Question 2 (f) - write function Defend()
def Defend(balloon):
    strength = int(input("Enter the strength of the opponent: "))
    balloon.ChangeHealth(-strength)
    print(f'You defended with {balloon.GetDefenceItem()}')
    if balloon.CheckHealth():
        print("Defence failed")
    else:
        print("Defence succeeded")
    return balloon


# Question 2 (g) (i) - write function call
Defend(Balloon1)
