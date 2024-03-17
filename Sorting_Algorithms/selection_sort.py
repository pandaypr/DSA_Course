numbers = [5,6,8,2,4,3]

def selection_sort(values):
    sorted_list = []

    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_val_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_val_index]:
            min_val_index = i
    return min_val_index

print(selection_sort(numbers))