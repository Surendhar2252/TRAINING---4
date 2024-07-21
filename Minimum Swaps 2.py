def minimumSwaps(arr):
    swaps = 0
    index = {v: i for i, v in enumerate(arr)}
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            to_swap_idx = index[i + 1]
            arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i]
            index[arr[to_swap_idx]] = to_swap_idx
            index[arr[i]] = i
            swaps += 1
            
    return swaps
