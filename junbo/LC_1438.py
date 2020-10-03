class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        1) use two deques to record the max/min of a sliding window
        2) sliding window start from i and ends at current index
        3) use increase/stay same length to record the maximun length
        '''
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for n in nums:
            while maxd and n > maxd[-1]: maxd.pop()
            while mind and n < mind[-1]: mind.pop()
            maxd.append(n)
            mind.append(n)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
        return len(nums) -i
