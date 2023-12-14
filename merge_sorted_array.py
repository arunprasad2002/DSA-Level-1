def merge_sorted_array(number1, m, number2, n):
    for i in range(n):
        number1[i + n] = number2[i]
    number1.sort()

    print(number1)





# 1,2,2,3,5,6


number1 = [1,2,3,0,0,0]
m = 3
number2 = [2,5,6]
n = 3
merge_sorted_array(number1, m, number2, n)