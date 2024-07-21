def pairs(k, arr):
    arr_set = set(arr)
    count = 0
    
    for number in arr:
        if number + k in arr_set:
            count += 1
            
    return count
