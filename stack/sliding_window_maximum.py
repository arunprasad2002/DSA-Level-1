def sliding_window_maximum(arr):
    n = len(arr)
    k = 4

    for i in range(n - k + 1):
        max_val = arr[i]
        for j in range(i, i + k):
            if arr[j] > max_val:
                max_val = arr[j]
        print(max_val, end=" ")

def next_greater_element(arr):
    ans = [0] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if not stack:
            ans[i] = len(arr)
        else:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def sliding_window_maximum_stack(arr, k):
    next_bigger_elements = next_greater_element(arr)
    ans = []

    for i in range(len(arr) - k + 1):
        j = i
        while next_bigger_elements[j] < i + k:
            j = next_bigger_elements[j]
        ans.append(arr[j])
    return ans


arr = [2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6]
ans = sliding_window_maximum_stack(arr, 4)
print(ans)
