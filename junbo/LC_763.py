class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        '''
        two pointer, 用的shallow copy
        '''
        t = {}
        for i, c in enumerate(S):
            if c not in t:
                t[c] = [i, i]
            else:
                end = t[c][1]
                t[c][1] = i
                for d in S[end+1:i]:
                    t[d] = t[c]
        temp = {start:end for start, end in t.values()}
        ret, q = [], 0
        while q < len(S):
            ret.append(temp[q] - q + 1)
            q = temp[q] + 1
        return ret
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        '''
        two passes
        '''
        rightmost = {c:i for i,c in enumerate(S)}
        left = right = 0
        ret = []
        for i, c in enumerate(S):
            right = max(right, rightmost[c])
            if i == right:
                ret.append(right - left + 1)
                left = right + 1
        return ret
    
                
        
