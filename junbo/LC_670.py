class Solution:
    def maximumSwap(self, num: int) -> int:
        # help random access digit and swap
        i, D = 1, list(str(num))
        # first first decreasing
        while i < len(D) and D[i-1] >= D[i]: 
            i += 1
        # swap A, B: A in [:i], B in [i:]
        # B is the rightest duplicate of the largest element in [i:]
        # A is the leftest element < B
        if i < len(D):
            p1, p2 = 0, str(num).rfind(max(D[i:]))
            while p1 < i-1 and D[p1] >= D[p2]:
                p1 += 1
            D[p1], D[p2] = D[p2], D[p1]
        return int(''.join(D))
