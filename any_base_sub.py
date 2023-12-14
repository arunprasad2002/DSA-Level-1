def any_base_sub(base, number1, number2):
    ans = 0
    carry = 0
    power = 1
    while number2 > 0:
        digit_1 = number1 % 10
        number1 = number1 // 10
        digit_2 = number2 % 10
        number2 = number2 // 10
        digit = 0
        digit_2 = digit_2 + carry
        if digit_2 >= digit_1:
            carry = 0
            digit = digit_2 - digit_1
        else:
            carry = -1
            digit = digit_2 + base - digit_1
        ans = ans + digit * power
        power = power * 10
    print(ans)

any_base_sub(8,256, 1212)