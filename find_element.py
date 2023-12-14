def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            print(i)
            return
    print(-1)



numbers = [15,30,40,4,11,9]
find_element(numbers, 40)