class Solution:
def numDistinct(self, s: str, t: str) -> int:
    '''
    T[i,j]: number of subseqs in s[:i] of t[:j]
                len(t) + 1
    len(s)+1    100000000
                1
                1
                1
                1
    '''
    M = [[0] * (len(t) + 1) for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        M[i][0] = 1
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                M[i][j] = M[i-1][j-1] + M[i-1][j]
            else:
                M[i][j] = M[i-1][j]
    return M[-1][-1]
