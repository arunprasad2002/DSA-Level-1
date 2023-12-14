def any_base_to_decimal(number, base):
    power = 1
    ans = 0
    while number != 0:
        digit = number % 10
        number = number // 10
        ans += digit * power
        power = power * base
    print(ans)

any_base_to_decimal(1172, 8)