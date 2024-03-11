"""
Recurrsive but runs very slowly, O(n^2) time complexity and O(n) Space Complexity
def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(20))"""

#This can be solved using Memoization i.e., Dictionary with keys and value

def fib(n, memo = {}):
    if (n in memo):
        return memo.get(n)
    if n<=2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(50))