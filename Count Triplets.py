from collections import defaultdict

def countTriplets(arr, r):
    count = 0
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
        
    return count
