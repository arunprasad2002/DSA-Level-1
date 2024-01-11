def operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

def prefix_evaluation_conversion(expression):
    values = []
    infix = []
    postfix = []

    for char in reversed(expression):
        if char in ['+', '-', '*', '/']:
            operator = char
            # Process values
            value_a = values.pop()
            value_b = values.pop()
            value = operation(value_a, value_b, operator)
            values.append(value)

            # Process infix
            infix_a = infix.pop()
            infix_b = infix.pop()
            infix_expression = "(" + infix_a + operator + infix_b + ")"
            infix.append(infix_expression)

            # Process postfix
            postfix_a = postfix.pop()
            postfix_b = postfix.pop()
            postfix_expression = postfix_a + postfix_b + operator
            postfix.append(postfix_expression)
        else:
            number = int(char)
            values.append(number)
            infix.append(char)
            postfix.append(char)
    return values.pop(), infix.pop(), postfix.pop()



expression = '-+2/*6483'
ans = prefix_evaluation_conversion(expression)
print(ans)
