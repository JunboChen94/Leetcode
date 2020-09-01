class Solution:
    # 1) backtracking
    # canWin: the so called guarantee to win is there is that first can find a
    # step lead to guarantee wining, not no matter what the first player plays
    # so it is second player can not find any step to win
    def canWin(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i:i+2] == '++' and not self.canWin(s[:i]+'--'+s[i+2:]):
                return True
        return False
    
    # return any(s[i:i+2] == '++' and not self.canWin(s[:i]+'--'+s[i+2:]) for i in range(len(s) - 1))
