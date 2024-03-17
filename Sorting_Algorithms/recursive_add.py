num = [5,6,8,2,4,3]

def add(numbers):
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0]+remaining_sum

print(add(num))