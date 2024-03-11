#This recursive method takes longer time to execute
#The complexity of this method is O(n^m) and the space complexity is O(m)

"""def canSum(targetsum, arr):
    if (targetsum == 0): return True
    if (targetsum < 0): return False
    for num in arr:
        reminder = targetsum - num

        if canSum(reminder, arr) == True:
            return True
    return False"""

#This solution runs faster by reducing the complexity to O(m*n) and the space complexity is O(m)
def canSum(targetsum, arr, memo = {}):
    if targetsum in memo : return memo.get(targetsum)

    if (targetsum == 0): return True
    if (targetsum < 0): return False
    
    for num in arr:
        reminder = targetsum - num

        if canSum(reminder, arr, memo) == True:
            memo[targetsum] = True
            return True
    memo[targetsum] = False
    return False 

print(canSum(300, [7,14]))