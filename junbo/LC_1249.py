class Solution:
def minRemoveToMakeValid(self, s: str) -> str:
    '''
    Based on the idea of stack, but actually not using stack, instead use a count
    '''
    parentheses = ["(", ")"]
    for i in range(2):
        ret = []
        count = 0
        for c in s:
            if c != parentheses[1-i]:
                if c == parentheses[i]:
                    count += 1
                ret.append(c)
            elif count:
                ret.append(c)
                count -= 1
        s = ''.join(ret)[::-1]
    return s
    '''
    Since we only need to push when meet "(" in the first pass
    We could fully leverage stack by pushing index
    The help us to use one pass instead of two.
    And making str to list to help us get rid of char at index i at constant time
    "".join(s) to convert it back to string
    '''
    s = list(s)
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack):
                stack.pop()
            else:
                s[i] = ""
    for i in stack: s[i] = ""
    return "".join(s)
    
