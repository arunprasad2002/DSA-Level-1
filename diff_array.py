def diff_array(arr1, arr2):

    max_len = max(len(arr1), len(arr2))
    result = [0] * (max_len)
    i = len(arr1) - 1
    j = len(arr2) - 1
    k = len(result) - 1
    carry = 0
    digit = 0
    while k >= 0:
        arr1_value = arr1[i] if i >= 0 else 0
        if arr2[j] + carry >= arr1_value:
            digit = arr2[j] + carry - arr1_value
            carry = 0
        else:
            digit = arr2[j] + carry + 10 - arr1_value
            carry = -1

        result[k] = digit

        j -= 1
        k -= 1
        i -= 1


    print(result)

arr1 =  [1]
arr2 = [1,0,0]

diff_array(arr1, arr2)