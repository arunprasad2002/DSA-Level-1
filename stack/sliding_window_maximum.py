def sliding_window_maximum(arr):
    n = len(arr)
    k = 4  # window size

    for i in range(n - k + 1):
        window = arr[i:i+k]
        max_val = max(window)
        print(max_val, end=" ")

arr = [2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6]
sliding_window_maximum(arr) 
