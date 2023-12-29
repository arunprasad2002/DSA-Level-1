
def next_smaller_left(arr):
    ans = []
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if not stack:
            ans.append(0)
        else:
            ans.append(stack[-1] + 1)
        stack.append(i)
    return ans


def next_smaller_right(arr):
    ans = [0] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if not stack:
            ans[i] = len(arr) - 1
        else:
            ans[i] = stack[-1] - 1
        stack.append(i)
    return ans


def max_area_histogram(arr):
    width = [0] * len(arr)
    area = [0] * len(arr)
    right = next_smaller_right(arr)
    left = next_smaller_left(arr)
    for i in range(len(arr)):
        width[i] = right[i] - left[i] + 1
    
    for i in range(len(arr)):
        area[i] = width[i] * arr[i]
    
    ans = max(area)

    return ans

#      0  1  2  3  4  5  6
arr = [6, 2, 5, 4, 5, 1, 6]
test_arr = [1,1]
ans = max_area_histogram(test_arr)
print(ans)

