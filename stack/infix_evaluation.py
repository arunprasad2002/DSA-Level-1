def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0  # Assuming operators not defined in your precedence function are lowest priority

def operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

def infix_evaluation(expression):
    operands = []
    operators = []

    index = 0
    while index < len(expression):
        char = expression[index]

        if char == "(":
            operators.append(char)
        elif char.isdigit():
            operand = int(char)
            operands.append(operand)
        elif char == ')':
            while operators[-1] != '(':
                operator = operators.pop()
                b = operands.pop()
                a = operands.pop()
                value = operation(a, b, operator)
                operands.append(value)
            operators.pop()  # Remove the '('

        elif char in ['+', '-', '*', '/']:
            while operators and operators[-1] != '(' and precedence(char) <= precedence(operators[-1]):
                operator = operators.pop()
                b = operands.pop()
                a = operands.pop()
                value = operation(a, b, operator)
                operands.append(value)
            operators.append(char)

        index += 1

    while operators:
        operator = operators.pop()
        b = operands.pop()
        a = operands.pop()
        value = operation(a, b, operator)
        operands.append(value)

    return operands[0]

expression = '(5+2)/1'
ans = infix_evaluation(expression)
print(ans)
