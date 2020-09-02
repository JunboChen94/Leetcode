class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Idea is similar to two sum, but fix one value and search two sum in the rest
        But here we could have duplicate values, if we use memorization, we also
        need to memorize which values combination we have used.
        Therefore, we move to two pointers, the direct intuition is O(n) does not
        exist, so we can use sort without affacting time complexity.
        '''
        #1) i update to avoid duplicate, so i is first value v, l and r can explore
        # all possible remaining values, so we could have 1 v, 2v or 3v.
        # i can only be the first element having value v, otherwise there would be duplicate.
        ret = []
        nums.sort()
        i = 0
#        while i < len(nums) - 2:
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while r > i and nums[r] == nums[r - 1]:
                        r -= 1
                    while l < len(nums) - 2 and nums[l] == nums[l+1]:
                        l += 1
                    r -= 1
                    l += 1
#            while i < len(nums) - 2 and nums[i] == nums[i+1]:
#                 i += 1
#            i += 1
        return ret
    
