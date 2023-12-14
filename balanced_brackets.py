def handel_close(stack, ch):
    if len(stack) == 0:
        return False
    if stack[-1] != ch:
        return False
    if stack[-1] == ch:
        stack.pop()
        return True

def blanced_brackets(str):
    stack = []
    for ch in str:
        if ch == '[' or ch == '(' or ch == '{':
            stack.append(ch)
        if ch == ']':
            ans = handel_close(stack, '[')
            if ans == False:
                return False
        if ch == ')':
            ans = handel_close(stack, '(')
            if ans == False:
                return False
        if ch == '}':
            ans = handel_close(stack, '{')
            if ans == False:
                return False

    if len(stack) > 0:
        return False
    else:
        return True


str = '[(a+b)+{(c+d)*(e/f)}]'
str2 = '[(a+b)+{(c+d)*(e/f)]}'
ans = blanced_brackets(str2)
print(ans)