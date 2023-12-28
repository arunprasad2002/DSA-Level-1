# solution by index in stack
def ngei(arr):
    ans = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            ans[index] = arr[i] 
        stack.append(i)
    return ans

def ngeli(arr):
    ans = [-1] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            ans[index] = arr[i]
        stack.append(i)
    return ans
# solution by value in stack

def nge(arr):
    ans = [0] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]

        stack.append(arr[i])
    return ans


def ngel(arr):
    ans = [0] * len(arr)
    stack = []
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans
arr = [1,3,2,4]
ans = ngel(arr)
print(ans)


