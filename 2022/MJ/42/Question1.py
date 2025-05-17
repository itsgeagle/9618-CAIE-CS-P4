# Question 1 (a) - declare array and variable
StackData = [0 for i in range(10)]  # integer
StackPointer = 0  # integer


# Question 1 (b) - write procedure OutputValues()
def OutputValues():
    global StackPointer
    global StackData

    print(f'Pointer - {StackPointer}')
    print("Stack values:")
    for value in StackData:
        print(value)


# Question 1 (c) = write function Push()
def Push(NewValue):
    global StackPointer
    global StackData

    if StackPointer >= 10:
        return False

    StackData[StackPointer] = NewValue
    StackPointer += 1
    return True


# Question 1 (d) (i) - write main program code
for i in range(11):
    userIn = int(input("Enter a number to push onto the stack: "))
    print("Number was successfully added." if Push(userIn) else "The stack is full!")
OutputValues()


# Question 1 (e) (i) - write function Pop()
def Pop():
    global StackPointer
    global StackData

    if StackPointer == 0:
        return -1

    StackPointer -= 1
    return StackData[StackPointer]


# Question 1 (e) (ii) = amend main program code
Pop()
Pop()
OutputValues()
