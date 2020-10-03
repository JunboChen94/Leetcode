class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        my: sliding window, three pointers
        
        (nums[k:j]; k in [i, j]) + nums[j, current] is nice array
        so at each iteration, update i and j
        and increment by j - i
        """
        j = i = count = ret = 0
        for n in nums:
            if n%2: count += 1
            if count == k:
                i = j
            while count == k:
                count -= 1 if nums[j] % 2 else 0
                j += 1
            ret += j - i
        return ret
        
        '''
        cleaner version
        '''
        i = count = ret = 0
        for j in range(len(nums)):
            if nums[j] & 1:
                k -= 1
                count = 0
            while k == 0:
                k += nums[i] & 1
                i += 1
                count += 1
            ret += count
        return ret
        
        '''
        two passes, extact k times = at most k times - at most k - 1 times
        Not as good as solutions above, since solutions above are one-pass
        '''
        def atMost(A: List[int], k: int) -> int:
            i = ret = 0
            for j in range(len(A)):
                if A[j] & 1:
                    k -= 1
                while k < 0:
                    k += A[i] & 1
                    i += 1
                ret += j - i + 1
            return ret
        
        return atMost(nums, k) - atMost(nums, k-1)
