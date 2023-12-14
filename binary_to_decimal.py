def binary_to_decimal(number):
    power = 1
    ans = 0
    while number != 0:
        digit = number % 10
        number = number // 10
        ans += digit * power
        power = power * 2
    print(ans)

binary_to_decimal(100)
