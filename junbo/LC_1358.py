class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        xxxxxxxx@@, 所有从@@前开始的subtring均满足条件，只需要记录最后一个x的位置，且该位置需增大
        '''
        ret = i = 0
        d = {c : 0 for c in 'abc'}
        for j in range(len(s)):
            d[s[j]] += 1
            while all(d.values()):
                d[s[i]] -= 1
                i += 1
            ret += i
        return ret
