class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search to find the pivot
        lo, hi = 0, len(nums)
        # binary search for the the first value <= nums[-1], first value < nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= nums[0]: # nums[mid] > nums[-1]
                lo = mid + 1
            else:
                hi = mid
        # binary search in two sections
        for l, r in [(0, hi), (hi, len(nums))]:
            candidate = bisect.bisect_left(nums, target, l, r)
            if candidate < len(nums) and nums[candidate] == target:
                return candidate
        return -1
