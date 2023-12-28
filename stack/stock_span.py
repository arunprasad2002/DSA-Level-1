def stock_span_brute_force(arr):
    ans = []
    for i in range(len(arr)):
        span = 1
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                span += 1
        ans.append(span)
    return ans

    
def stock_span(arr):
    ans = []
    stack = []
    for i in range(len(arr)):
        while len(stack) > 0 and arr[stack[-1]] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(i + 1)
        else:
            ans.append(i - stack[-1])
        stack.append(i)
    
    return ans



arr = [100, 80, 60, 70, 60, 75, 85]
ans = stock_span(arr)
print(ans)

# Output: 1 1 1 2 1 4 6