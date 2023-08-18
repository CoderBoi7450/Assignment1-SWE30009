
# Calculate the the result based on the value of a, b and the operations given
def testResult(symbolOne, symbolTwo, a, b):
    firstOperation = OperationOne(symbolOne, a,b)
    secondOperation = OperationSecond(symbolTwo, firstOperation)
    return secondOperation

def OperationOne(symbol, a, b):
    if symbol == "+":
        return a + b
    elif symbol == "-":
        return a - b
    elif symbol == "*":
        return a * b
    elif symbol == "/":
        return a / b
    
def OperationSecond(symbol, a):
    if symbol == "+":
        return a + 2
    elif symbol == "-":
        return a - 2
    elif symbol == "*":
        return a * 2
    elif symbol == "/":
        return a / 2
    
# Find possible values of A that does not meet the testing objective in a range
def PossibleValues(rangeValue):
    b = 1
    possibleOperator = ["+", "-", "*", "/"]
    testCaseResult = []

    for i in range (-rangeValue,rangeValue):
        for symbolOne in possibleOperator:
            for symbolTwo in possibleOperator:
                correctAnswer = testResult("-", "*", i, b)
                if symbolOne == "-" and symbolTwo == "*":
                    continue
                result = testResult(symbolOne, symbolTwo, i, b)
                testCaseResult.append(result)

        if correctAnswer in testCaseResult:
            print("value of a " + str(i))
            print("Correct Answer " + str(correctAnswer))
            print(str(testCaseResult) + "\n")
        testCaseResult.clear()
    
     


if __name__ == "__main__":
    PossibleValues(10000)