def maxSubarray(arr):
    max_contiguous = current = arr[0]
    max_non_contiguous = 0 if all(v <= 0 for v in arr) else 0
    
    for num in arr:
        max_non_contiguous = max(max_non_contiguous, max_non_contiguous + num) if num > 0 else max_non_contiguous
        current = max(num, current + num)
        max_contiguous = max(max_contiguous, current)
        
    return [max_contiguous, max_non_contiguous]
