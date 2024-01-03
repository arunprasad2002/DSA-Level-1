def sliding_window_maximum(arr):
    n = len(arr)
    k = 4

    for i in range(n - k + 1):
        max_val = arr[i]
        for j in range(i, i + k):
            if arr[j] > max_val:
                max_val = arr[j]
        print(max_val, end=" ")

arr = [2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6]
sliding_window_maximum(arr)
