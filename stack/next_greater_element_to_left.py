def next_greater_element_to_left(arr):
    for i in range(len(arr)):
        greater_found = False
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i]:
                print(arr[j])
                greater_found = True
                break
        if not greater_found:
            print(-1)

def next_greater_element_to_left_better(arr):
    ans = []
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and arr[i] < stack[-1]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(arr[i])
        stack.append(arr[i])
    return ans

def next_greater_element_to_left_itirative(arr):
    ans = []
    stack = []
    for i in range(len(arr)):
        while len(stack) > 0 and arr[i] > stack[-1]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    return ans



arr = [1, 3, 2, 4]
ans = next_greater_element_to_left_itirative(arr)
print(ans)
