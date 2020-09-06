class Solution:
def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    '''
    Binary Search: discussion, not as good as mine
    '''
    n, m = binaryMatrix.dimensions()
    res = m
    for j in range(n):
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if binaryMatrix.get(j, mid) < 1:
                lo = mid + 1
            else:
                hi = mid
        res = min(res, lo)
    return res if res < m else -1
    '''
    Mine is better, do not need to run full binary for each every row
    binary search need to find first column where there exist row making [row, column] none zero
    O(MlogN)
    '''
    H, W = binaryMatrix.dimensions()
    candidate_rows = list(range(H))
    l, r = 0, W
    while l < r:
        mid = (l + r) // 2
        nonzero_rows = [candidate_row for candidate_row in candidate_rows if binaryMatrix.get(candidate_row, mid)]
        if len(nonzero_rows):
            candidate_rows = nonzero_rows
            r = mid
        else:
            l = mid + 1
    return (-1, r)[r < W]
    
    '''
    Maze like solution O(M+N)
    '''
    M, N = binaryMatrix.dimensions()
    r, c = 0, N - 1
    ret = -1
    while r < M and c >= 0:
        if binaryMatrix.get(r, c):
            ret = c
            c -= 1
        else:
            r += 1
    return ret
