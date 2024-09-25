# Question 1 (a) - define class node
class node:
    def __init__(self, theData, theNextNode):  # Create constructor
        self.data = theData  # Define value of data
        self.nextNode = theNextNode  # Define value of pointer to next node in linked list


# Question 1 (b) - Declare linkedList using given values
linkedList = [
    node(1, 1),
    node(5, 4),
    node(6, 7),
    node(7, -1),
    node(2, 2),
    node(0, 6),
    node(0, 8),
    node(56, 3),
    node(0, 9),
    node(0, -1)
]
startPointer = 0  # Define startPointer as given
emptyList = 5  # Define emptyList as given


# Question 1 (c) (i) - write procedure outputNodes()
def outputNodes(theList, pointer):
    while pointer != -1:  # Check if at end of linked list
        print(theList[pointer].data)  # Output data stored at node
        pointer = theList[pointer].nextNode  # Use pointer at node to find position of next node


# Question 1 (c) (ii) - call outputNodes()
outputNodes(linkedList, startPointer)


# Question 1 (d) (i) - write procedure addNode()
def addNode(linkedList, startPointer):
    global emptyList

    data = input("Enter the data to add: ")  # Prompt input of data value to be appended to lis
    if emptyList < 0 or emptyList > 9:  # Check if list is full
        return False
    else:
        emptyListNext = linkedList[emptyList].nextNode  # Store pointer to second item in empty list (to assign later)
        linkedList[emptyList] = node(int(data), -1)  # Assign value to first item in empty list

        currentPointer = startPointer
        lastPointer = currentPointer  # Variable which will be used to store pointer to last value in list

        while currentPointer != -1:  # Iterate through linkedlist to find last position
            lastPointer = currentPointer  # Save value of pointer at each iteration
            currentPointer = linkedList[currentPointer].nextNode

        linkedList[lastPointer].nextNode = emptyList  # Change last item to point to new last item
        emptyList = emptyListNext  # Set new value of emptyList
        return True


# Question 1 (d) (ii) - edit program to add more function calls
retVal = addNode(linkedList, startPointer)  # Store return from addNode to indicate success status
print("Node added successfully" if retVal else "Node not added")  # Toggle output based on success status
outputNodes(linkedList, startPointer)
print(emptyList)
