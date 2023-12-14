def base_sum(base, number1, number2):
    ans = 0
    carry = 0
    power = 1
    while number1 > 0 or number2 > 0 or carry > 0:

        digit1 = number1 % 10
        digit2 = number2 % 10
        number1 = number1 // 10
        number2 = number2 // 10
        sum = digit1 + digit2 + carry
        carry = sum // base
        sum = sum % base
        ans += sum * power
        power = power * 10

    print(ans)

base_sum(8, 236, 754)