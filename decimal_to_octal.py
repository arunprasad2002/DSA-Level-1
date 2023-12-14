def decimal_to_octal(number):
    power = 1
    ans = 0
    while number != 0:
        remainder = number % 8
        number = number // 8
        ans += remainder * power
        power = power * 10
    print(ans)

decimal_to_octal(694)
