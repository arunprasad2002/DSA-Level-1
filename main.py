def pattern1(number):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print("")

def pattern2(number):
    for i in range(number, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print(" ")

def pattern3(number):
    for i in range(1, number + 1):
        spaces = number - i
        for j in range(1, number + 1):
            if j <=  spaces:
                print(" ", end="")
            else:
                print("*", end="")
        print("")

def pattern4(number):
    for i in range(number, 0, -1):
        spaces = number - i
        for j in range(1, number + 1):
            if j <= spaces:
                print(" ", end="")
            else:
                print("*", end="")
        print(" ")

def pattern5(number):
    spaces = number // 2
    stars = 1
    for i in range(1, number + 1):

        for j in range(1, spaces + 1):
            print(" ", end="")
        for k in range(1, stars + 1):
            print("*", end="")

        if i <= number // 2:
            spaces = spaces - 1
            stars = stars + 2
        else:
            spaces = spaces + 1
            stars = stars - 2
        print("")
def pattern6(number):
    spaces = 1
    stars = number // 2 + 1
    for i in range(1, number + 1):
        for start in range(1, stars + 1):
            print("*", end="")
        for space in range(1, spaces + 1):
            print(" ", end="")
        for start in range(1, stars + 1):
            print("*", end="")
        if i <= number // 2:
            spaces += 2
            stars = stars - 1
        else:
            spaces -= 2
            stars = stars + 1
        print("")

def pattern7(number):
    for i in range(number, 0, -1):
        spaces = number - i
        stars = 1
        for space in range(1, spaces + 1):
            print(" ", end="")
        for star in range(1, stars + 1):
            print("*", end="")
        print("")

def pattern7V2(number):
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

def pattern8(number):
    for i in range(number, 0, -1):
        for j in range(1, number + 1):
            if i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
def pattern8V2(number):
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if i + j == number + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

def pattern9(number):
    for row in range(1, number + 1):
        for col in range(1, number + 1):
          if row == col or row + col == number + 1:
              print("* \t",end="")
          else:
              print("\t", end="")
        print("")

def pattern10(number):
    outer_spaces = number // 2
    inner_spaces = -1
    for i in range(1, number + 1):
        # print(outer_spaces, inner_spaces)
        for outer in range(1, outer_spaces + 1):
            print("\t", end="")

        print("* \t", end="")

        for inner in range(1, inner_spaces + 1):
            print("\t", end="")

        if i > 1 and i < number:
            print("* \t", end="")

        print("")
        if i <= number // 2:
            outer_spaces -= 1
            inner_spaces += 2
        else:
            outer_spaces += 1
            inner_spaces -= 2

def pattern10V2(number):
    spaces = number // 2
    inner_spaces = -1
    for row in range(1, number + 1):

        for outer_space in range(1, spaces + 1):
            print("\t", end="")

        print("* \t", end="")

        for inner in range(1, inner_spaces + 1):
            print("\t", end="")

        if row > 1 and row < number:
            print("* \t", end="")

        print("")


        if row <= number // 2:
            spaces -= 1
            inner_spaces += 2
        else:
            spaces += 1
            inner_spaces -= 2

def pattern11(number):
    value = 1
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(value , end="\t")
            value += 1

        print("")

def pattern12(number):
    first_value = 0
    second_value = 1
    for i in range(1, number + 1):

        for j in range(1, i + 1):
            print(first_value, end="\t")
            third_value = first_value + second_value
            first_value = second_value
            second_value = third_value

        print("")

def pattern13(number):
    for i in range(0, number + 1):
        icj = 1
        for j in range(0, i + 1):
            print(icj, end="\t")
            icjp1 = icj * (i - j) // (j + 1)
            icj = icjp1
        print()


def pattern14(number):
    for i in range(1, 10 + 1):
        print(f"{number} x {i} = {number * i}")


def pattern15(number):
    spaces = number // 2
    stars = 1
    value = 1
    for i in range(1, number + 1):
        for space in range(1,spaces + 1):
            print("\t", end="")
        c_value = value
        for star in range(1, stars + 1):
            print(c_value, end="\t")
            if star <= stars // 2:
                c_value += 1
            else:
                c_value -= 1
        if i <= number // 2:
            stars += 2
            spaces -= 1
            value += 1
        else:
            stars -= 2
            spaces += 1
            value -= 1
        print()

def pattern16(number):
    star = 1
    space = number * 2 - 3
    value = 1
    for i in range(1, number + 1):
        c_value = value
        for j in range(1, star + 1):
            print(c_value, end="\t")
            c_value += 1
        for k in range(1, space + 1):
            print("\t", end="")
        if i == number:
                star -= 1
                c_value -= 1
        for j in range(1, star + 1):
            c_value -= 1
            print(c_value, end="\t")
        if i <= number:
            star += 1
            space -= 2
        print()



def pattern17(number):
    spaces = number // 2
    stars = 1
    temp_star = number
    temp_space = 0
    for i in range(1, number + 1):

        if i == number // 2 + 1:
            for space in range(1, temp_space + 1):
                print("\t", end="")
            for star in range(1, temp_star + 1):
                print("*", end="\t")
        else:
            for space in range(1, spaces + 1):
                print("\t", end="")
            for star in range(1, stars + 1):
                print("*", end="\t")
        if i <= number // 2:
            stars += 1
        else:
            stars -= 1
        print()

def pattern17V2(number):
    spaces = number // 2
    stars = 1
    for i in range(1, number + 1):
        for space in range(1, spaces + 1):
            if i == number // 2 + 1:
                print("*", end="\t")
            else:
                print("\t", end="")
        for star in range(1, stars + 1):
            print("*", end="\t")
        if i <= number // 2:
            stars += 1
        else:
            stars -= 1
        print()

def pattern_up_arrow(number):
    spaces = number // 2
    stars = 1
    for i in range(1, number + 1):
        for space in range(1, spaces + 1):
            print("\t", end="")
        for star in range(1, stars + 1):
            print("*", end="\t")
        if i <= number // 2:
            stars += 2
            spaces -= 1
        else:
            stars = 1
            spaces = 2
        print()


def pattern18(number):
    stars = number
    spaces = 0
    for i in range(1, number + 1):
        for space in range(1, spaces + 1):
            print("\t", end="")
        for star in range(1, stars + 1):
            if i > 1 and i <= number // 2 and star > 1 and star < stars:
                print("\t", end="")
            else:
                print("*", end="\t")
        if i <= number // 2:
            spaces += 1
            stars -= 2
        else:
            stars += 2
            spaces -= 1
        print()



def pattern19(number):
    for row in range(1, number + 1):
        for col in range(1, number + 1):
            if row == 1:
                if col == number or col <= number // 2 + 1:
                    print("*", end="\t")
                else:
                    print("\t", end="")
            elif row <= number // 2:
                if col == number // 2 + 1 or col == number:
                    print("*", end="\t")
                else:
                    print("\t", end="")
            elif row == number // 2 + 1:
                print("*", end="\t")
            elif row < number:
                if col == 1 or col == number // 2 + 1:
                    print("*", end="\t")
                else:
                    print("\t", end="")
            else:
                if col >= number // 2 + 1 or col == 1:
                    print("*", end="\t")
                else:
                    print("\t", end="")
        print()

def pattern20(number):
    for row in range(1, number + 1):
        for col in range(1, number + 1):
            if col == 1 or col == number:
                print("*", end="\t")
            elif row > number // 2  and (row == col or row + col == number + 1):
                print("*", end="\t")
            else:
                print("\t", end="")
        print()


pattern20(21)
