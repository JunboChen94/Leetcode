class Solution:
def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    '''
    sum of substring think about accumulate
    '''
    if k == 0:
        return any((x1==0 and x2==0) for x1, x2 in zip(nums, nums[1:]))
    mods = [i % k for i in itertools.accumulate([0] + nums)]
    T = {}
    for i, mod in enumerate(mods):
        if mod in T:
            if i > T[mod] + 1: return True
        else:
            T[mod] = i
    return False
