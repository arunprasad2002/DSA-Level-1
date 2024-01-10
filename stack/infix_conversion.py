def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '/' or operator == '*':
        return 2
    else:
        return 0

def infix_conversion(expression):
    postfix = []
    prefix = []
    operators = []

    for char in expression:
        if char == '(':
            operators.append(char)
        elif char.isdigit() or char.isalpha():
            postfix.append(char)
            prefix.append(char)
        elif char == ")":
            while operators[-1] != "(":
                operator = operators.pop()
                # process prefix
                b = prefix.pop()
                a = prefix.pop()
                prefix_value = operator + a + b
                prefix.append(prefix_value)

                # process postfix
                b = postfix.pop()
                a = postfix.pop()
                postfix_value = a + b + operator
                postfix.append(postfix_value)
            operators.pop() #Removing (
        elif char in ['+', '-', '*', '/']:
            while operators and char != '(' and precedence(char) <= precedence(operators[-1]):
                operator = operators.pop()
                # process prefix
                b = prefix.pop()
                a = prefix.pop()
                prefix_value = operator + a + b
                prefix.append(prefix_value)

                # process postfix
                b = postfix.pop()
                a = postfix.pop()
                postfix_value = a + b + operator
                postfix.append(postfix_value)
            operators.append(char)

    while operators:
                operator = operators.pop()
                # process prefix
                b = prefix.pop()
                a = prefix.pop()
                prefix_value = operator + a + b
                prefix.append(prefix_value)

                # process postfix
                b = postfix.pop()
                a = postfix.pop()
                postfix_value = a + b + operator
                postfix.append(postfix_value)   
    return prefix[0], postfix[0]

        




expression = '(3+a)*b-(c/2)'
ans = infix_conversion(expression)
print(ans)