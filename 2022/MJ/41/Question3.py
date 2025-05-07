# Question 3 (a) - declare arrays and variables
QueueArray = ["" for i in range(10)]  # string
HeadPointer = 0  # integer
TailPointer = 0  # integer
NumberOfItems = 0  # integer


# Question 3 (b) - write function Enqueue()
def Enqueue(Queue, Head, Tail, NumItems, InputData):

    if NumItems == 10:
        return False, Queue, Head, Tail, NumItems

    Queue[Tail] = InputData

    if Tail >= 9:
        Tail = 0
    else:
        Tail += 1

    NumItems += 1
    return True, Queue, Head, Tail, NumItems


# Question 3 (c) - write function Dequeue()
def Dequeue(Queue, Head, Tail, NumItems):

    if NumItems == 0:
        return False, Queue, Head, Tail, NumItems

    RetVal = Queue[Head]
    Head = Head + 1
    if Head >= 9:
        Head = 0
    NumItems -= 1

    return RetVal, Queue, Head, Tail, NumItems


# Question 3 (d) (i) - write main program code
for i in range(11):
    newVal = input("Enter a value: ")
    Success, QueueArray, HeadPointer, TailPointer, NumberOfItems = Enqueue(QueueArray, HeadPointer, TailPointer, NumberOfItems, newVal)
    print("Successfully added." if Success else "Unsuccessful.")

RetVal, QueueArray, HeadPointer, TailPointer, NumberOfItems = Dequeue(QueueArray, HeadPointer, TailPointer, NumberOfItems)
print(f'First value: {RetVal}')
RetVal, QueueArray, HeadPointer, TailPointer, NumberOfItems = Dequeue(QueueArray, HeadPointer, TailPointer, NumberOfItems)
print(f'Second value: {RetVal}')
