

def serach(arr, target):
    for value in arr:
        if value == target:
            return False
    return True

def unique(arr, target):
    count = 0
    for value in arr:
        if target == value:
            count += 1
    if count > 1:
        return False
    return True

def contain_duplicates(arr, target):
    count = 0
    for value in arr:
        if value == target:
            count += 1
    if count > 1:
        return True
    else:
        return False


def remove_duplicates(arr):
    ans = []
    for value in arr:
        if not contain_duplicates(arr, value):
            ans.append(value)
    print(ans)


def findDifference(arr1, arr2):
    ans1 = []
    ans2 = []
    ans = []

    for i in range(len(arr1)):
        digit1 = arr1[i]
        digit2 = arr2[i]
        if serach(arr2, digit1):
            ans1.append(digit1)
        if serach(arr1, digit2):
            ans2.append(digit2)
    ans.append(list(set(ans1)))
    ans.append(list(set(ans2)))
    print(ans)











arr1 = [1,2,3,3]
arr2 = [1,1,2,2]


print(findDifference(arr1, arr2))
