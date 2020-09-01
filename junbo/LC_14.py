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
