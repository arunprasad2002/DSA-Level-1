def reverse_array(arr):
    temp_array = []
    for i in range(len(arr) - 1, -1, -1):
        temp_array.append(arr[i])
    for j in range(len(temp_array)):
        arr[j] = temp_array[j]
    print(arr)

def swap(index_1, index_2, arr):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

def reverse_swap_array(arr):
    first_index = 0
    last_index = len(arr) - 1
    while first_index != last_index:
        swap(first_index, last_index, arr)
        first_index += 1
        last_index -= 1
    print(arr)



arr = [1,2,3]
reverse_swap_array(arr)