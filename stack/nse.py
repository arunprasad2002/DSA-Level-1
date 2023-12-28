# nearset smallest element to left

def nse_brute_force(arr):
    ans = []
    for i in range(len(arr)):
        found_smaller = False
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                found_smaller = True
                ans.append(arr[j])
                break
        if not found_smaller:
                ans.append(-1)
    return ans

def nsel(arr):
     ans = []
     stack = []
     for i in range(len(arr)):
          while len(stack) > 0 and stack[-1] > arr[i]:
               stack.pop()
          if len(stack) == 0:
               ans.append(-1)
          else:
               ans.append(stack[-1])
          stack.append(arr[i])
     
     return ans


def nser_brute_force(arr):
     ans = []
     for i in range(len(arr)):
          found_smaller = False
          for j in range(i + 1, len(arr)):
              if arr[j] < arr[i]:
                   ans.append(arr[j])
                   found_smaller = True
                   break
          if not found_smaller:
               ans.append(-1)
     return ans

def nser(arr):
     ans = []
     stack = []
     for i in range(len(arr) - 1, -1, -1):
          while len(stack) > 0 and stack[-1] > arr[i]:
               stack.pop()
          if len(stack) == 0:
               ans.append(-1)
          else:
               ans.append(stack[-1])
          stack.append(arr[i])
     ans.reverse()
     return ans


    

arr = [4,5,2,10,8]
ans = nser(arr)
print(ans)

# ans = [2, 2, -1, 8, -1]