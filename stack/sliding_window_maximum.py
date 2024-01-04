from collections import deque 

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

def sliding_window_maximum_linear(arr, k):
    que = deque()
    left = 0
    right = 0
    ans = []
    
    while right < len(arr):
        # pop smaller values from que
        while que and arr[que[-1]] < arr[right]:
           que.pop() 
        que.append(right)
        # remove left value from window
        if left > que[0]:
            que.popleft()

        if (right + 1) >= k:
            ans.append(arr[que[0]])
            left += 1
        right += 1
    return ans





arr = [8,7,6,9]
ans = sliding_window_maximum_linear(arr, 2)
print(ans)
