class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        leverage the fact that python's sort is inplace
        '''
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key = lambda x: x.split(' ')[0])
        letters.sort(key = lambda x: x.split(' ')[1:])
        # combine these two
        letters.sort(key = lambda x: (x.split(' ')[1:], x.split(' ')[0]))
        return letters + digits
