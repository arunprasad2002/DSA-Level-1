def decimato_to_base(number, base):
    power = 1
    ans = 0
    while number != 0:
        digit = number % base
        number = number // base
        ans += digit * power
        power = power * 10
    print(ans)


decimato_to_base(634, 2)