def find_celebrity(peoples):
    n = len(peoples)
    
    for i in range(n):
        is_celebrity = True
        
        # Check if person i knows anyone
        for j in range(n):
            if peoples[i][j] == 1:
                is_celebrity = False
                break
        
        # Check if everyone else knows person i
        if is_celebrity:
            for k in range(n):
                if k != i and peoples[k][i] == 0:
                    is_celebrity = False
                    break
        
        if is_celebrity:
            return i
    
    return -1

peoples = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]

ans = find_celebrity(peoples)
print(ans)
