stack = []

def push(element):
    if not stack or element <= stack[-1]:
        stack.append(element)

def get_min():
    if not stack:
        return -1
    else:
        return stack[-1]

def pop():
    if stack:
        stack.pop()

push(10)
push(2)
pop()
push(5)

print(get_min())
