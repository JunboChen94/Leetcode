class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        '''
        nums[i] saves the maximum sum ends at i
        q saving the promising sum could be used at later step
        '''
        q = collections.deque()
        for i in range(len(nums)):
            nums[i] += q[0] if q else 0
            while q and nums[i] > q[-1]:
                q.pop()
            if nums[i] > 0:
                q.append(nums[i])
            if i >= k and q and q[0] == nums[i-k]:
                q.popleft()
        return max(nums)
