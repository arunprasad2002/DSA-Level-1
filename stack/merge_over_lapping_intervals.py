def merge_overlapping_intervals(arr):
    arr.sort()  # Sort intervals based on the start time
    
    merged_intervals = []
    current_interval = arr[0]

    for interval in arr[1:]:
        if current_interval[1] >= interval[0]:  # Overlapping intervals
            current_interval[1] = max(current_interval[1], interval[1])
        else:
            merged_intervals.append(current_interval)
            current_interval = interval

    merged_intervals.append(current_interval)

    return merged_intervals




arr = [[1,3],[2,6],[8,10],[15,18]]
ans = merge_overlapping_intervals(arr)
print(ans)
