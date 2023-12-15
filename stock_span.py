def stock_span(arr):
    stack = []
    ans = []
    for i in range(len(arr)):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            ans.append(i + 1)
        else:
            span = i - stack[-1]
            ans.append(span)
        stack.append(i)
    return ans
arr = [100, 80, 60, 70, 60, 75, 85]
ans = stock_span(arr)
print(ans)