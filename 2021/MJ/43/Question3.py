# Question 3 (a) - declare class TreasureChest
class TreasureChest:

    # Write attribute declarations as comments, as requested by question paper
    # Private question : String
    # Private answer : Integer
    # Private points : Integer

    def __init__(self, theQuestion, theAnswer, thePoints):  # Create constructor
        self.question = theQuestion  # Define value of question
        self.answer = theAnswer  # Define value of answer
        self.points = thePoints  # Define number of points

    # Question 3 (c) (i) - write method getQuestion()
    def getQuestion(self):
        return self.question

    # Question 3 (c) (ii) - write method checkAnswer()
    def checkAnswer(self, userAnswer):
        return userAnswer == self.answer  # Return whether they match

    # Question 3 (c) (iii) - write method getPoints()
    def getPoints(self, attempts):
        if attempts == 1:
            return self.points
        elif attempts == 2:
            return self.points // 2
        elif attempts == 3 or attempts == 4:
            return self.points // 3
        else:
            return 0


# Question 3 (b) - write procedure readData()
arrayTreasure = []


def readData():
    filename = "treasureChestData.txt"  # Store name of text file
    try:  # Ensure that file is opened without error
        file = open(filename, "r")
        rawData = file.readlines()
        for i in range(0, len(rawData), 3):  # Iterate through every set of 3 adjacent values in the list
            question = rawData[i].strip('\n')
            answer = rawData[i + 1].strip('\n')
            points = rawData[i + 2].strip('\n')
            arrayTreasure.append(TreasureChest(question, answer, points))  # Create and append TreasureChest object
        file.close()  # Close file after done using
    except IOError:  # Check for input/output error
        print("File not found")


# Question 3 (c) (iv) - write main program code
readData()
choice = int(input("Enter a treasure chest to open: "))
while not 0 < choice < 6:  # Check if choice is a valid question
    choice = int(input("The number must be between 1 and 5 inclusive. Enter a treasure chest to open: "))
attempts = 0
result = False
while not result:
    userAnswer = input(arrayTreasure[choice - 1].getQuestion())
    result = arrayTreasure[choice - 1].checkAnswer(userAnswer)
    attempts += 1
print(f'You score {int(arrayTreasure[choice - 1].getPoints(attempts))} points!')
