class Solution:
def findAnagrams(self, s: str, p: str) -> List[int]:
    '''
    Counter based sliding window
    '''
    counter = defaultdict(int)
    for c in p:
        counter[c] += 1
    start = end = 0
    ret = []
    while end < len(s):
        if counter[s[end]] > 0:
            counter[s[end]] -= 1
            end += 1
            if end - start == len(p):
                ret.append(start)
        elif start == end:
            start += 1
            end += 1
        else:
            counter[s[start]] += 1
            start += 1
    return ret
