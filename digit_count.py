def digit_count(number):
    for i in range(len(number)):
        ans = False
        digit = i
        times = int(number[i])
        count = 0
        for j in range(len(number)):
            if digit == int(number[j]):
                count += 1
        if count != times:
            return False
    return True





ans = digit_count("5210010007")
print(ans)