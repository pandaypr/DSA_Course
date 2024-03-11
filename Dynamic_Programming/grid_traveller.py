"""Runs Slowly with O(2^m+n) in Time and O(m+n) in Space
def gridTraveler(m,n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    return gridTraveler(m-1,n) + gridTraveler(m,n-1)

"""
#Memoizing to improve time Complexity
#Now the complexity is O(m*n) in Time and O(m+n) in Space
def gridTraveler(m,n, memo = {}):
    key = str(m) + ',' + str(n)
    
    if key in memo: return memo.get(key)

    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    
    memo[key] = gridTraveler(m-1,n, memo) + gridTraveler(m,n-1, memo)

    return memo[key]



print(gridTraveler(18,18))