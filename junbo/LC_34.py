class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1) 
        ret = [-1, -1]
        
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if l < len(nums) and nums[l] == target:
            ret[0] = l
        else:
            return ret
        
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        ret[1] = r
        
        return ret
        
        # 2)
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect(nums, target, lo=lo)-1] if target in nums[lo:lo+1] else [-1, -1]
