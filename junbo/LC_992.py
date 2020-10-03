class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        '''
        exact K = atMost(K) - atMost(K-1)
        '''
        def atMost(A: List[int], K: int) -> int:
            d = collections.defaultdict(int)
            i = ret = 0
            for j in range(len(A)):
                d[A[j]] += 1
                while len(d) > K:
                    d[A[i]] -= 1
                    if d[A[i]] == 0:
                        del d[A[i]]
                    i += 1
                ret += j - i + 1
            return ret
        return atMost(A, K) - atMost(A, K-1)
