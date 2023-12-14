def ngetr(arr):
    ans = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                ans.append(arr[j])
                break
    ans.append(-1)
    print(ans)


def ngetr_stack(arr):
    stack = []
    ans = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    ans = ans[::-1]  # Reverse the list to get the correct order
    print(ans)

def next_greater_element_right(arr):
    stack = []
    ans = [-1] * len(arr)
    for i in range(len(arr)):
        while len(stack) != 0 and arr[i] > arr[stack[len(stack) - 1]]:
            index = stack[len(stack) - 1]
            ans[index] = arr[i]
            stack.pop()
        stack.append(i)
    return ans




numbers = [1, 3, 2, 4]
ngetr_stack(numbers)
