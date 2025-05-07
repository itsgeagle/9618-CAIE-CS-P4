# Question 2 (a) (i) - write class Card and constructor
class Card:

    # Write attribute declarations as requested by question paper
    # Private Number : Integer
    # Private Colour : String

    def __init__(self, Number, Colour):
        self.Number = Number
        self.Colour = Colour

    # Question 2 (a) (ii) - write getter methods
    def GetNumber(self):
        return self.Number

    def GetColour(self):
        return self.Colour


# Question (a) (iii) - declare Card objects with requested data
OneRed = Card(1, 'red')
TwoRed = Card(2, 'red')
ThreeRed = Card(3, 'red')
FourRed = Card(4, 'red')
FiveRed = Card(5, 'red')
OneBlue = Card(1, 'blue')
TwoBlue = Card(2, 'blue')
ThreeBlue = Card(3, 'blue')
FourBlue = Card(4, 'blue')
FiveBlue = Card(5, 'blue')
OneYellow = Card(1, 'yellow')
TwoYellow = Card(2, 'yellow')
ThreeYellow = Card(3, 'yellow')
FourYellow = Card(4, 'yellow')
FiveYellow = Card(5, 'yellow')


# Question 2 (b) (i) write class Hand and constructor
class Hand:

    # Write attribute declarations as requested by question paper
    # Private Cards : Card[10]
    # Private FirstCard : Integer
    # Private NumberCards : Integer

    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.Cards = [Card1, Card2, Card3, Card4, Card5]
        self.FirstCard = 0
        self.NumberCards = 5

    # Question 2 (b) (i) - write method GetCard()
    def getCard(self, index):
        return self.Cards[index]


# Question 2 (b) (iii) - declare Hand objects with requested data
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)


# Question 2 (c) (i) - write function CalculateValue()
def CalculateValue(playerHand):
    score = 0
    for i in range(5):

        currentCard = playerHand.getCard(i)  # Fetch card from hand
        score += currentCard.GetNumber()  # Add card's number to total

        if currentCard.GetColour() == 'red':
            score += 5
        elif currentCard.GetColour() == 'blue':
            score += 10
        elif currentCard.GetColour() == 'yellow':
            score += 15

    return score


# Question 2 (c) (ii) - write function calls
P1Score = CalculateValue(Player1)
P2Score = CalculateValue(Player2)
if P1Score > P2Score:
    print('Player 1 wins!')
elif P1Score < P2Score:
    print('Player 2 wins!')
else:
    print('Draw!')