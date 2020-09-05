class Solution:
def validPalindrome(self, s: str) -> bool:
    '''
    at the very begining, I wish to directly use
    sum(map(operator.nq, s, s[::-1])) in [0,2]
    but that work only for change one digit rather than delete one digit
    digit one digit has many cornercase, abc, adddddd
    '''
    
    '''
    The below solution is O(n^2), too slow, time exceeded
    for i in range(len(s)):
        temp = s[:i] + s[i+1:]
        if temp == temp[::-1]: return Truie
    return s == s[::-1]
    '''
    '''
    The solution below is O(n), inspired by other's s[l:r] and s[l+1:r+1] checking,
    posted on discussion session
    '''
    class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
            l += 1
            r -= 1
        return True
