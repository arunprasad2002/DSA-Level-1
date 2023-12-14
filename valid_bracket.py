def invalid_bracket(s):
    stack = []
    for ch in s:
        if ch == ')':
            if stack and stack[-1] == '(':
                print(True)
                return
            else:
                while stack and stack[-1] != '(':
                    stack.pop()
                stack.pop()
        else:
            stack.append(ch)

# Example usage:
# valid_bracket("someString")

str = "(a+b)+((a+b))"
invalid_bracket(str)