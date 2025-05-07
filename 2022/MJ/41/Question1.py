# Question 1 (a) - declare arrays
FileData = [[""] * 2 for i in range(11)]  # string


# Question 1 (b) - write procedure ReadHighScores()
def ReadHighScores():
    global FileData

    file = open("HighScore.txt", 'r')
    for i in range(0, 10):
        FileData[i][0] = file.readline().strip('\n')
        FileData[i][1] = file.readline().strip('\n')

    file.close()


# Question 1 (c) - write procedure OutputHighScores()
def OutputHighScores():
    global FileData
    for playerData in FileData:
        print(f'{playerData[0]} {playerData[1]}')


# Question 1 (d) (i) - write main program code
ReadHighScores()
OutputHighScores()

# Qeestion 1 (e) (i) - query use
newName = input("Enter your username: ")
while not len(newName) == 3:
    newName = input("Enter your username: ")

score = -1
while score < 1 or score > 100000:
    score = int(input("Enter your score: "))


# Question 1 (e) (ii) - write procedure Arrange()
def Arrange(Username, Score):
    global FileData
    for i in range(0, 10):
        if Score > int(FileData[i][1]):
            Temp1 = FileData[i][0]
            Temp2 = FileData[i][1]
            FileData[i][0] = Username
            FileData[i][1] = Score
            Count = i + 1
            while Count < 10:
                Second1 = FileData[Count][0]
                Second2 = FileData[Count][1]
                FileData[Count][0] = Temp1
                FileData[Count][1] = Temp2

                Temp1 = Second1
                Temp2 = Second2
                Count += 1
            break


# Question 1 (e) (iii) - amend main program
Arrange(newName, score)
OutputHighScores()


# Question 1 (f) - write procedure WriteTopTen()
def WriteTopTen():
    global FileData

    file = open("NewHighScore.txt", 'w')
    for i in range(0, 10):
        file.write(FileData[i][0])
        file.write("\n")
        file.write(FileData[i][1])
        file.write("\n")

    file.close()
