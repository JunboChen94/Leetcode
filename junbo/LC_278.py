# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        Binary Search
        """
        l, r = 1, n + 1
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
        '''
        Python vocabulary
        '''
        class wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(wrap(), False, 0, n)
        
