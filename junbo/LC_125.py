class Solution:
def isPalindrome(self, s: str) -> bool:
    '''
    My two pointer solution:
    I choose not use while in while l < r to make code clearner
    besides, for example: ';;;;;;;;;;;;;;', my code l and r would both travese just
    after l >= r, if while is used, l would have to go to len(s) and r go to -1,
    additional index check is also needed.
    '''
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True
    '''
    the following is also cool
    '''
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
