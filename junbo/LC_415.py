class Solution:
def addStrings(self, num1: str, num2: str) -> str:
    '''
    Similar to LC_2 add two number
    '''
    addends = num1, num2
    i = 1
    carry, ret = 0, []
    while addends or carry:
        carry += sum(int(x[-i]) for x in addends)
        ret.append(carry % 10)
        carry //= 10
        i += 1
        addends = [x for x in addends if i <= len(x)]
    ret = [str(d) for d in ret][::-1]
    return ''.join(ret)
