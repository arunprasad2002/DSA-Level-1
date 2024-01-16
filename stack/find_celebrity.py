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

def find_celebrityV2(peoples):
    incoming = [0] * len(peoples)
    outgoing = [0] * len(peoples)
    for i in range(len(peoples)):
        for j in range(len(peoples)):
            if peoples[i][j] == 1:
                incoming[j] += 1
                outgoing[i] += 1
    for k in range(len(incoming)):
        if incoming[k] == len(peoples) - 1 and outgoing[k] == 0:
            return k
    
    return -1

def find_celebrityV3(peoples):
    celebrity = 0
    
    # Find a potential celebrity
    for i in range(1, len(peoples)):
        if peoples[celebrity][i] == 1:
            celebrity = i
    
    # Check if the potential celebrity meets the criteria
    for j in range(len(peoples)):
        if j != celebrity and (peoples[celebrity][j] == 1 or peoples[j][celebrity] == 0):
            return -1
    
    return celebrity



peoples = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]

ans = find_celebrityV2(peoples)
print(ans)
