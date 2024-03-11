#Has higher Complexity
#Brute Force:  O(n^m * m) in Time and space Complexity: O(m*m)
"""
def bestSum(targetsum, numbers):
    if (targetsum == 0): return []
    if (targetsum < 0): return None

    shortestCombination = None
    for num in numbers:
        reminder = targetsum - num
        reminderCombination = bestSum(reminder, numbers)
        if reminderCombination !=None:
            reminderCombination.append(num)
            #If the reminderCombination is shorter than shortestCombination then update it
            if  shortestCombination == None or len(reminderCombination) < len(shortestCombination):
                shortestCombination = reminderCombination

    return shortestCombination
"""
#Memoized code with O(m*n*m)==>O(m^2 m )==>O(mn) and space complexity is O(m^2)
def bestSum(targetsum, numbers, memo = {}):
    if targetsum in memo : return memo.get(targetsum)

    if (targetsum == 0): return []
    if (targetsum < 0): return None

    shortestCombination = None

    for num in numbers:
        reminder = targetsum - num
        reminderCombination = bestSum(reminder, numbers, memo)

        if reminderCombination !=None:
            reminderCombination.append(num)
            #memo[targetsum] = reminderCombination
            #If the reminderCombination is shorter than shortestCombination then update it
            if  shortestCombination == None or len(reminderCombination) < len(shortestCombination):
                shortestCombination = reminderCombination
    
    memo[targetsum] = shortestCombination
    return shortestCombination


print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))