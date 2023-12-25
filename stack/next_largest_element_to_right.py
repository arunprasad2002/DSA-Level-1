
def next_greater_element_right(arr):
    ans = [0] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and arr[i] > stack[-1]:
            stack.pop()
        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans

def next_greater_element_rightV2(arr):
    ans = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            ans[index] = arr[i]
        stack.append(i)
    return ans


arr = [1,0,2,3]
ans = next_greater_element_rightV2(arr)
print(ans)