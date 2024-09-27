# Question 3 (a) - declare ArrayNodes, RootPointer and FreeNodes
ArrayNodes = [[0 for X in range(3)] for Y in range(20)]  # use "for... in" structure to create an empty 3x20 list
RootPointer = -1
FreeNode = 0


# Question 2 (b) write procedure AddNode()
def AddNode(arr, root, free):
    data = int(input("Enter the data you wish to add: "))

    if free <= 19:  # Check if list is full
        arr[free] = [-1, data, -1]  # Add data to first node in free list

        if root == -1:  # Check if list is empty
            root = 0
        else:
            Placed = False  # Flag to check if placement of node has been found
            CurrentNode = root  # Variable to store current node being looked at
            while not Placed:
                if data < arr[CurrentNode][1]:  # Check if data should go to left
                    if arr[CurrentNode][0] == -1:  # Check is left pointer is empty
                        arr[CurrentNode][0] = free
                        Placed = True
                    else:
                        CurrentNode = arr[CurrentNode][0]  # Set CurrentNode to next left-side node
                else:
                    if arr[CurrentNode][2] == -1:  # Check if right pointer is empty
                        arr[CurrentNode][2] = free
                        Placed = True
                    else:
                        CurrentNode = arr[CurrentNode][2]  # Set CurrentNode to next right-side node
        free += 1  # Set start of free list to next position
    else:
        print("Tree is full")

    return arr, root, free  # Return modified values (including pointers, so they can be updated)


# Question 3 (c) - write procedure PrintAll()
def PrintAll(arr):
    for node in arr:
        print(f'{node[0]} {node[1]} {node[2]}')


# Question 3 (d) (i) - write main program code

for i in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)

PrintAll(ArrayNodes)


# Question 3 (e) (i) - write procedure InOrder()
def InOrder(arr, root):
    if arr[root][0] != -1:
        InOrder(arr, arr[root][0])
    print(str(arr[root][1]))
    if arr[root][2] != -1:
        InOrder(arr, arr[root][2])


InOrder(ArrayNodes, RootPointer)
