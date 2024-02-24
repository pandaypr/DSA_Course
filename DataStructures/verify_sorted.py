def  verify_sorted(list):
    n = len(list)

    if n == 0 or n ==1:
        return True
    
    return list[0] < list[1] and  verify_sorted(list[1:])
