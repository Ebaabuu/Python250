from arraystack import ArrayStack
from arrayqueue import ArrayQueue

def evaluate(operand1, operand2, operator):
    """Evaluate the operation for the given operands and operator.
    
    Args:
        operand1 (int or float): The first operand.
        operand2 (int or float): The second operand.
        operator (str): The operator as a string ('+', '-', '*', '/').
        
    Returns:
        int or float: The result of the operation.
    """

    # STEP 1
    if operator not in "+/*-":
        raise TypeError("ERROR: Invalid operator.")

    if operator == "/" and operand2 == 0:
        raise ZeroDivisionError("ERROR: Cannot divide by zero.")

    if operator == "+":
        return operand1 + operand2

    elif operator == "-":
        return operand1 - operand2

    elif operator == "*":
        return operand1 * operand2

    else: # /
        return float(operand1) / operand2

def main():
    """Main program to evaluate a post-fix expression."""
    expression = input("Enter a post-fix expression using only integer operands: ")
    expressionQueue = ArrayQueue()
    operandStack = ArrayStack()
    
    # Enqueue elements into expressionQueue
    # STEP 2
    for e in expression.split():
        expressionQueue.add(e)

    # Evaluate the expression
    # STEP 3
    while len(expressionQueue) > 0:
        poppedValue = expressionQueue.pop()
        if poppedValue.isdigit():
            operandStack.push(int(poppedValue))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()

            try:
                result = evaluate(operand2, operand1, poppedValue)

            except ZeroDivisionError as exc:
                print(exc)
                exit()

            except TypeError as exc:
                print(exc)
                exit()

            operandStack.push(result)
    
    # If we reach this stage and the stack doesn't contain 1 value,
    # something has gone wrong. Likely we didn't have a valid postfix 
    # expression to begin with.
    if operandStack.isEmpty() or len(operandStack) > 1:
        print("ERROR: Invalid expression.")
    else:
        print(f"The result of the expression is: {operandStack.pop()}")

if __name__ == "__main__":
    main()
    
