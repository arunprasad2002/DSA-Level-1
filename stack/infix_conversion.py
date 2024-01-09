def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    else:
        return 0
def compute(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == '/':
        return a / b
def infix_evaluation(expression):
    operators = []
    operands = []
    for char in expression:
        if char == "(":
            operators.append(char)
        elif char.isdigit():
            operands.append(int(char))
        elif char == ")":
            while operators[-1] != "(":
                operator = operators.pop()
                b = operands.pop()
                a = operands.pop()
                value = compute(a, b, operator)
                operands.append(value)
            operators.pop()
        elif char in ['+', '-', '*', '/']:
            while operators and operators[-1] != "(" and precedence(char) <= precedence(operators[-1]):
                operator = operators.pop()
                b = operands.pop()
                a = operands.pop()
                value = compute(a, b, operator)
                operands.append(value)
            operators.append(char)
    while len(operators) != 0:
        operator = operators.pop()
        b = operands.pop()
        a = operands.pop()
        value = compute(a, b, operator)
        operands.append(value)
    
    return operands[0]

    

ans = infix_evaluation('5+4')
print(ans)