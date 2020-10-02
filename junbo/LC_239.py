class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        We scan the array from 0 to n-1, keep "promising" elements in the deque. The algorithm is amortized O(n) as each element is put and polled once.

        At each i, we keep "promising" elements, which are potentially max number in window [i-(k-1),i] or any subsequent window. This means

        If an element in the deque and it is out of i-(k-1), we discard them. We just need to poll from the head, as we are using a deque and elements are ordered as the sequence in the array

        Now only those elements within [i-(k-1),i] are in the deque. We then discard elements smaller than a[i] from the tail. This is because if a[x] <a[i] and x<i, then a[x] has no chance to be the "max" in [i-(k-1),i], or any other subsequent window: a[i] would always be a better candidate.

        As a result elements in the deque are ordered in both sequence in array and their value. At each step the head of the deque is the max element in [i-(k-1),i]
        '''
        q = collections.deque()
        out = []
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q += [i]
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                out += [nums[q[0]]]
        return out
