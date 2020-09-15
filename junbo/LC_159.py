class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''
        Sliding window + HashTable
        '''
        T = defaultdict(int)
        l = r = 0
        ret = 0
        while r < len(s):
            T[s[r]] += 1
            r += 1
            while len(T) > 2:
                T[s[l]] -= 1
                if T[s[l]] == 0:
                    del T[s[l]] # T.pop[s[l]]
                l += 1
            ret = max(ret, r - l)
        return ret
        '''
        Above is not necessary
        这里很巧要仔细想想
        满足条件sliding window变大，不满足条件sliding window长度不变
        所以没必要keep track of largest len，sliding window大小right - left本身就是
        record，因为其只会增大不会缩小
        若之后遇到更大的，left刚到更大的substring的开始时候，只会right++，left不会++
        sliding window扩大
        '''
        left = 0
        right = 0
        counts = defaultdict(int)
        while right < len(s):
            counts[s[right]] += 1
            right += 1
            if len(counts) > 2:
                counts[s[left]] -= 1
                if not counts[s[left]]:
                    del counts[s[left]]
                left += 1
        return right -left
