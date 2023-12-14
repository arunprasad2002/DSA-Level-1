def digit_freq(number, target):
    freq = 0
    while number != 0:
        digit =  number % 10
        if digit == target:
            freq += 1
        number = number // 10
    return freq

freq = digit_freq(95439629, 9)
print(freq)