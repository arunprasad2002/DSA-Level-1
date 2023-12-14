def span_of_array(numbers):
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number
    return max - min

arr = [15,30,40,4,11,9]
span = span_of_array(arr)
print(span)
