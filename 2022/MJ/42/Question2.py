# Question 2 (a) - initialize array
import random as r
ArrayData = [[r.randint(1, 100) for i in range(10)] for j in range(10)]


# Question 2 (b) (ii) - write procedure OutputArray()
def OutputArray():
    global ArrayData
    for row in ArrayData:
        thisLine = ""
        for item in row:
            thisLine += str(item) + " "
        print(thisLine)


print("Before:")
OutputArray()

# Question 2 (b) (i) - write bubble sort code
ArrayLength = 10
for x in range(ArrayLength):
    for y in range(ArrayLength - 1):
        for z in range(ArrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z + 1]:
                Temp = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z + 1]
                ArrayData[x][z + 1] = Temp

print("After:")
OutputArray()


# Question 2 (c) (i) - write function BinarySearch()
def BinarySearch(SearchArray, Lower, Upper, SearchValue):

    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)

    return -1


# Question 2 (c) (ii) - write main program code
Search1 = int(input())
print(BinarySearch(ArrayData, 0, 9, Search1))
Search2 = int(input())
print(BinarySearch(ArrayData, 0, 9, Search2))
