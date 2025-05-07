# Question 3 (a) - declare and initialize ArrayNodes[]
ArrayNodes = []
for i in range(20):
    ArrayNodes.append([-1, -1, -1])

# Question 3 (b) - store data and initialize variables
ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]
FreeNode = 6
RootPointer = 0


# Question 3 (c) - write function SearchValue()
def SearchValue(Root, ValueToFind):

    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:  # Case where value has been found
            return Root
        elif ArrayNodes[Root][1] == -1:  # End of list has been reached
            return -1

        if ArrayNodes[Root][1] > ValueToFind:
            return SearchValue(ArrayNodes[Root][0], ValueToFind)  # Set search root to next left node
        elif ArrayNodes[Root][1] < ValueToFind:
            return SearchValue(ArrayNodes[Root][2], ValueToFind)  # Set search root to next right node


# Question 3 (d) - write procedure PostOrder()
def PostOrder(RootNode):

    if ArrayNodes[RootNode][0] != -1:
        PostOrder(ArrayNodes[RootNode][0])
    if ArrayNodes[RootNode][2] != -1:
        PostOrder(ArrayNodes[RootNode][2])

    print(ArrayNodes[RootNode][1])


# Question 3 (e) (i) - write main program
ValFound = SearchValue(RootPointer, 15)
if ValFound != -1:
    print(f"Value 15 was found at {ValFound}.")
else:
    print("Value 15 was not found in tree.")
PostOrder(RootPointer)