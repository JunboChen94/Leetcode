class Solution:
def isAnagram(self, s: str, t: str) -> bool:
    '''
    HashTable
    '''
    T = defaultdict(int)
    for c in s:
        T[c] += 1
    for c in t:
        count[c] -= 1
        if count[c] < 0:
            return False
    return True
    '''
    sorted
    '''
    return sorted(s) == sorted(t)
