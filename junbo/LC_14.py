class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1) initial
        if len(strs) < 1:
            return ''
        ret = []
        index = 0
        while True:
            comm = strs[0][index:index+1]
            for i in range(1, len(strs)):
                if strs[i][index:index+1] != comm:
                    return "".join(ret)
            if not comm:
                return "".join(ret)
            ret.append(comm)
            index += 1
        return "".join(ret)
        
        # 2) the solution above does not use the condition that longest prefix must be
        # prefix of shortest string
        if not strs:
            return ""
        # the above corner case handling is required, since [] can not be passed as
        # min's argument
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for other in strs:
                if other[i] != shortest[i]:
                    return shortest[:i]
        return shortest
