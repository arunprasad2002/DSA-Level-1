def sum_array(numbers1, numbers2):
    i = len(numbers1) - 1
    j = len(numbers2) - 1
    k = max(len(numbers1), len(numbers2)) - 1
    result = [0] * (k + 1)  # Fix the size of the result array
    carr = 0

    while k >= 0 or carr != 0:  # Fix the loop condition
        digit = carr

        if i >= 0:
            digit += numbers1[i]
        if j >= 0:
            digit += numbers2[j]

        carr = digit // 10
        digit = digit % 10

        result[k] = digit

        i -= 1
        j -= 1
        k -= 1

    print(result)

# Example usage
numbers1 = [1, 2, 3]
numbers2 = [1]
sum_array(numbers1, numbers2)
