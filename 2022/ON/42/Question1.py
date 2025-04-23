# Question 1 (a) - declare variables and arrays
Jobs = []  # -> global integer, 100 by 2 elements
NumberOfJobs = 0  # -> global integer


# Question 1 (b) - write procedure Initialise()
def Initialise():
    global Jobs
    global NumberOfJobs
    for i in range(0, 100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0


# Question 1 (c) - write procedure AddJob()
def AddJob(JobNumber, Priority):
    global Jobs
    global NumberOfJobs

    if NumberOfJobs < 100:
        Jobs[NumberOfJobs] = [JobNumber, Priority]
        NumberOfJobs += 1
        print("Added")
    else:
        print("Not Added")


# Question 1 (d) - write main program code
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)


# Question 1 (e) - write procedure InsertionSort()
def InsertionSort():
    global Jobs
    global NumberOfJobs
    for i in range(1, NumberOfJobs):
        Current1 = Jobs[i][0]
        Current2 = Jobs[i][1]
        while i > 0 and Jobs[i - 1][1] > Current2:
            Jobs[i][0] = Jobs[i - 1][0]
            Jobs[i][1] = Jobs[i - 1][1]
            i = i - 1
        Jobs[i][0] = Current1
        Jobs[i][1] = Current2


# Question 1 (f) - write procedure PrintArray()
def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(0, NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")

# Question 1 (g) (i) - write rest of main program code
InsertionSort()
PrintArray()