#Time Complexity: O(n^m * m) & Space Complexity is O(m)
"""def howSum(targetsum, numbers):
    if (targetsum == 0): return []
    if (targetsum < 0): return None

    for let in numbers:
        reminder = targetsum - let

        reminderResult = howSum(reminder, numbers)
        if reminderResult != None:
            reminderResult.append(let)
            return reminderResult
    return None"""

#Improved code has a Time Cimplexity of O(m*n*m) and Space complexity is O(m*m)

def howSum(targetsum, numbers, memo={}):
    if targetsum in memo: return memo.get(targetsum)
    if (targetsum == 0): return []
    if (targetsum < 0): return None

    for let in numbers:
        reminder = targetsum - let
        reminderResult = howSum(reminder, numbers, memo)

        if reminderResult != None:
            reminderResult.append(let)
            memo[targetsum] = reminderResult
            return memo[reminderResult]
    memo[targetsum] = None
    return None


print(howSum(300, [7,14]))


