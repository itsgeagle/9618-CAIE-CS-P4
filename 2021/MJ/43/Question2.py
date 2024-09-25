# Question 2 (a) - declare and initialize arrayData
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


# Question 2 (b) (i) - write function linearSearch()
def linearSearch(param):
    for value in arrayData:  # Iterate through every element in arrayData
        if param == value:  # If a match is found
            return True  # Return true and exit loop

    return False  # If nothing was found during iteration, return false and exit loop


# Question 2 (b) (ii) - allow user to input and search
userIn = int(input("Enter a number: "))
retVal = linearSearch(userIn)
print("Value found in list!" if retVal else "Value not found!")


# Question 2 (c) - write function bubbleSort()
def bubbleSort():
    for x in range(0, 10):  # Go through n + 1 iterations, where n is length of list
          for y in range(0, 9):  # Iterate through indices of list
            if arrayData[y] < arrayData[y + 1]:  # Check if pair is unordered
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp  # Complete swap of two elements
