# Question 2 (a) - write class Picture and constructor
class Picture:

    # Write attribute declarations as requested by question paper
    # Private Description : String
    # Private Width : Integer
    # Private Height : Integer
    # Private FrameColour : String

    def __init__(self, desc, widthVal, heightVal, colour):  # Create constructor method
        self.Description = desc
        self.Width = widthVal
        self.Height = heightVal
        self.FrameColour = colour

    # Question 2 (b) - write getter methods
    def getDescription(self):
        return self.Description

    def getHeight(self):
        return self.Height

    def getWidth(self):
        return self.Width

    def getColour(self):
        return self.FrameColour

    # Question 2 (c) - write SetDescription() method
    def setDescription(self, desc):
        self.Description = desc


# Question 2 (d) - declare array of type Picture with 100 elements
PictureArray = []  # Create an empty list
for i in range(100):  # Loop 100 times, to append 100 Picture objects
    PictureArray.append(Picture("", 0, 0, ""))  # Append an "empty" Picture object


# Question 2 (e) - write function ReadData()
def ReadData():
    global PictureArray

    filename = "Pictures.txt"
    counter = 0  # Store number of pictures in the array

    try:  # Run code in try block to catch any IOError in case of missing file
        file = open(filename)
        rawData = file.readlines()  # Use readlines() to obtain an array with every line stored in file

        for i in range(0, len(rawData), 4):  # Iterate through elements in chunks of 4 each (representing each picture)
            desc = rawData[i].strip('\n')  # Strip newline character
            width = int(rawData[i + 1].strip('\n'))  # Strip newline character and cast to Integer
            height = int(rawData[i + 2].strip('\n'))  # Strip newline character and cast to Integer
            colour = rawData[i + 3].strip('\n')  # Strip newline character
            temp = Picture(desc, width, height, colour)  # Create Picture object using data from file
            PictureArray[counter] = temp
            counter += 1

    except IOError:  # Error handling
        print("Could not find the file.")

    return counter


# Question 2 (f) - write function call and store number of pictures
NumPictures = ReadData()

# Question 2 (g) - write main program
FrameColour = input("Input the Frame Colour: ").lower()
MaxWidth = int(input("Input the Max Width: "))
MaxHeight = int(input("Input the Max Height: "))

print("This matches the following frames:")
for z in range(0, NumPictures):
    if (PictureArray[z].getColour() == FrameColour and PictureArray[z].getWidth() <= MaxWidth
            and PictureArray[z].getHeight() <= MaxHeight):  # Check for a matching frame
        print(f'{PictureArray[z].getDescription()}  {PictureArray[z].getWidth()}  {PictureArray[z].getHeight()}')
