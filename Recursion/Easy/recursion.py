def printFun(test):
    if (test < 1):
        return
    else:
        print(test, end=" ")
        printFun(test-1)  # Recursive call
        print(test, end=" ")
        return

# Driver Code
test = 3
printFun(test)