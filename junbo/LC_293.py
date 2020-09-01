class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        return [s[:i]+'--'+s[i+2:] for i in range(len(s)) if s[i:i+2] == '++']
