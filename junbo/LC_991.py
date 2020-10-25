class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y > X:
            Y = Y+1 if Y%2 else Y//2
            res += 1
        return res + X - Y
