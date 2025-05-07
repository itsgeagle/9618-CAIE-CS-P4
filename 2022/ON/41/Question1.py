# Question 1 (a) - declare array DataArray
DataArray = [0 for i in range(100)]  # Creates an array with the first 100 values being 0


# Question 1 (b) - write procedure ReadFile()
def ReadFile():
    global DataArray

    filename = "IntegerData.txt"

    try:  # Run code in try block to catch any IOError in case of missing file
        file = open(filename, "r")  # Access file in read mode
        index = 0  # Variable to store current position in array being accessed
        rawData = file.readlines()  # Obtain array with each line in file

        for line in rawData:  # Iterate through all lines in file
            DataArray[index] = int(line.strip('\n'))  # Strip newline character
            index += 1  # Increment index

        file.close()  # Close file object

    except IOError:  # Error handling
        print("Could not find the file.")


# Question 1 (c) - write function FindValues()
def FindValues():
    global DataArray

    searchVal = -1  # Set default value to negative to force while loop to run once

    while searchVal < 0 or searchVal > 100:
        searchVal = int(input("Enter a number between 0 and 100 (inclusive): "))
        numFound = 0  # Store number of times value was found
        for number in DataArray:
            if number == searchVal:
                numFound += 1

        return numFound


# Question 1 (d) (i) = write main program code to call ReadFile() and FindValues()
ReadFile()
print(f'Your requested value was found {FindValues()} times!')


# Question 1 (e) - write procedure BubbleSort()
def BubbleSort():
    global DataArray

    Sorted = False  # Flag variable that indicates whether array is done sorting

    while not Sorted:
        Sorted = True
        for i in range(len(DataArray)):  # Loop through all values in array
            for j in range(len(DataArray) - i - 1):  # Obtain indices being compared against
                if DataArray[j] > DataArray[j + 1]:  # Check if swap is required
                    DataArray[j], DataArray[j + 1] = DataArray[j + 1], DataArray[j]  # Swap adjacent values
                    Sorted = False  # Because change has been made, ensure that another pass occurs


BubbleSort()
print(f'Your Bubble sort was {DataArray}')  # As requested, output data
