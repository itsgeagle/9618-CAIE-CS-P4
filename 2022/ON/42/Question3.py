# Question 3 (a) - declare and initialize variables and arrays
Queue = [-1 for i in range(100)]
HeadPointer = -1
TailPointer = 0


# Question 3 (b) - write function Enqueue()
def Enqueue(data):
    global Queue, HeadPointer, TailPointer

    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = data
        TailPointer += 1
        return True
    return False


# Question 3 (c) - write Enqueue() function call
Success = False
for i in range(1, 21):
    Success = Enqueue(i)
if not Success:
    print("Unsuccessful")
else:
    print("Successful")


# Question 3 (d) -  write function RecursiveOutput()
def RecursiveOutput(Start):
    if Start == 0:
        return Queue[Start]
    else:
        return Queue[Start] + RecursiveOutput(Start - 1)


# Question 3 (e) (i) - write RecursiveOutput() call
print(str(RecursiveOutput(TailPointer - 1)))
