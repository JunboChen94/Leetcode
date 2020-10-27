class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        d = {'(':')','{':'}','[':']'}
        for c in s:
            if c in d:
                stack.append(d[c])
            else:
                if not len(stack) or stack.pop() != c:
                    return False
        return not len(stack)
