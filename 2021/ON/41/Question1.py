# Question 1 (a) - write function Unknown()

def Unknown(X, Y):  # Entire implementation is based on the given pseudocode
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    elif X == Y:  # Condensed pseudocode else-if to Python elif
        return 1
    else:
        print(X + Y)
        return Unknown(X - 1, Y) // 2


# Question 1 (b) (i) - write main program code
print(f'Unknown(10, 15) =>')
print(Unknown(10, 15))
print(f'Unknown(10, 10) =>')
print(Unknown(10, 10))
print(f'Unknown(15, 10) =>')
print(Unknown(15, 10))


# Question 1 (c) - write function IterativeUnknown() as an iterative version of function Unknown()
# By examining the algorithm of Unknown(), we can identify that there are three cases to be addressed here
# Case 1 - X < Y. In this case, output (X + Y), (X + Y + 1)... etc. for Y - X times, and return 2^(Y-X)
# Case 2 - X > Y. In this case, output (X + Y), (X + Y - 1)... etc. for X - Y times, and return (1//2)^(X-Y) (always 0)
# Case 3 - X = Y. In this case, output nothing, and return 1
def IterativeUnknown(X, Y):
    outVal = X + Y  # Define initial output value
    retVal = 1  # Define initial return value such that it matches case 3 (avoiding need for else clause below)
    if X < Y:  # Check for Case 1
        for i in range(X, Y):
            print(outVal)
            outVal += 1  # Generate (X + Y + 1), (X + Y + 2), ...
            retVal *= 2  # Generate 2^(Y-X)
    elif X > Y:
        for i in range(Y, X):
            print(outVal)
            outVal -= 1  # Generate (X + Y - 1), (X + Y - 2), ...
            retVal //= 2  # Generate (1//2)^(Y-X)
    return retVal


# Question 1 (d) (i) - write main program code to call iterative function
print(f'IterativeUnknown(10, 15) =>')
print(IterativeUnknown(10, 15))
print(f'IterativeUnknown(10, 10) =>')
print(IterativeUnknown(10, 10))
print(f'IterativeUnknown(15, 10) =>')
print(IterativeUnknown(15, 10))
