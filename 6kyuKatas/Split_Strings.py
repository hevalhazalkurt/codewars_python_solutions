
### Solution 1
def solution(s):
    ls = [s[i:i+2] for i,c in enumerate(s) if i % 2 == 0 and len(s[i:i+2]) == 2]
    if len(s) % 2 != 0:
        ls.append(s[-1] + "_")
    return ls



### Solution 2
def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]
