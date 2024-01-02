def maxWater(arr):
    max_left = [0] * len(arr)
    max_right = [0] * len(arr)
    max_left[0] = arr[0]
    max_right[len(arr) - 1] = arr[len(arr) - 1]
    wanter_unit = [0] * len(arr)
    for i in range(1, len(arr)):
        max_left[i] = max(arr[i], max_left[i - 1]) 
    for j in range(len(arr) - 2, -1, -1):
        max_right[j] = max(arr[j], max_right[j + 1])
    for k in range(len(arr)):
        wanter_unit[k] = min(max_right[k], max_left[k]) - arr[k]
    return sum(wanter_unit)
    




arr = [3, 0, 2, 0, 4]
ans = maxWater(arr)
print(ans)