import random
import sys

numbers = [5,6,8,2,4,3]

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        attempts +=1
        random.shuffle(values)
    print(attempts)
    return values

print(bogo_sort(numbers))