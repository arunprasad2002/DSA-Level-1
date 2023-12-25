def next_larget_element(arr):
    ans = []
    for i in range(len(arr)):
        current_element = arr[i]
        for j in range(i + 1, len(arr)):
            next_element = arr[j]
            if current_element < next_element:
                ans.append(next_element)
                break
    ans.append(-1)
    return ans



arr = [1,3,0,0,1,2,4]
ans = next_larget_element(arr)
print(ans)