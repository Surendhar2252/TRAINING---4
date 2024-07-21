from collections import defaultdict

def freqQuery(queries):
    elem_count = defaultdict(int)
    freq_count = defaultdict(int)
    result = []
    
    for op, val in queries:
        if op == 1:
            if elem_count[val]:
                freq_count[elem_count[val]] -= 1
            elem_count[val] += 1
            freq_count[elem_count[val]] += 1
        elif op == 2:
            if elem_count[val]:
                freq_count[elem_count[val]] -= 1
                elem_count[val] -= 1
                freq_count[elem_count[val]] += 1
        elif op == 3:
            result.append(1 if freq_count[val] > 0 else 0)
            
    return result
