def operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

def postfix_evaluation_conversion(expression):
    values = []
    infix = []
    prefix = []

    for char in expression:
        if char in ['+', '-', '*', '/']:
            # Process Values
            operator = char
            b = values.pop()
            a = values.pop()
            value = operation(a, b, operator)
            values.append(value)

            # Process infix expression
            infix_b = infix.pop()
            infix_a = infix.pop()
            infix_expression = "(" + infix_a + operator + infix_b + ")"
            infix.append(infix_expression)

            # Process prefix expression
            prefix_b = prefix.pop()
            prefix_a = prefix.pop()
            prefix_expression = operator + prefix_a + prefix_b
            prefix.append(prefix_expression)

        else:
            number = int(char)
            values.append(number)
            infix.append(char)
            prefix.append(char)
    
    return values.pop(), infix.pop(), prefix.pop()

expression = '34+2*'
ans = postfix_evaluation_conversion(expression)
print(ans)