class Solution:
def addBinary(self, a: str, b: str) -> str:
    '''
    general solution for add two integter and add two strings
    or we can make
    appends = list(a), list(b)
    int(x[-i]) -> pop(x)
    '''
    ret = []
    addends = a, b
    carry, i = 0, 1
    while addends or carry:
        carry += sum(int(x[-i]) for x in addends)
        ret.append(str(carry % 2))
        carry //= 2
        i += 1
        addends = [x for x in addends if i <= len(x)]
    return ''.join(ret)[::-1]
    
    '''
    The one-line solution below is just used to increase python vocabulary
    '''
    return bin(eval('0b' + a) + eval('0b' + b))[2:]
