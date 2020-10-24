class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or max(nums) == min(nums):
            return 0
        maxv, minv = max(nums), min(nums)
        binsize = (maxv - minv) // (len(nums)-1) or 1
        bins = [[None, None] for _ in range((maxv - minv) // binsize + 1)]
        for num in nums:
            print((num - minv) // binsize)
            b = bins[(num - minv) // binsize]
            b[0] = max(b[0], num) if b[0] else num
            b[1] = min(b[1], num) if b[1] else num
        bins = [b for b in bins if b[0]]
        return max([b2[1] - b1[0] for b1, b2 in zip(bins, bins[1:])])
        
