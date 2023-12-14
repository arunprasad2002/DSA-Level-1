def bar_chart(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    for height in range(max, 0, -1):
        for floor in numbers:
            if floor >= height:
                print("*", end="\t")
            else:
                print("\t", end="")
        print()



numbers = [3,1,0,7,5]
bar_chart(numbers)