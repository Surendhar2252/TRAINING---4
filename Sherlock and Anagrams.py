from collections import defaultdict

def sherlockAndAnagrams(s):
    count = 0
    substr_dict = defaultdict(int)
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = ''.join(sorted(s[i:j]))
            substr_dict[substr] += 1
            
    for key in substr_dict:
        count += (substr_dict[key] * (substr_dict[key] - 1)) // 2
        
    return count
