class Solution:
    '''
    simple DP O(1) memory
    '''
    def rob(self, nums: List[int]) -> int:
        p1, p2 = 0, 0
        for num in nums:
            p1, p2 = p2 + num, max(p1, p2)
        return max(p1, p2)
