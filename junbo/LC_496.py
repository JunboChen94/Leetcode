class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 用stack维持降序序列
        res = [-1 for _ in range(len(nums1))]
        d = {num:i for i, num in enumerate(nums1)}
        stack = [float(inf)]
        for n in nums2:
            while stack[-1] < n:
                small = stack.pop()
                if small in d:
                    res[d[small]] = n
            stack.append(n)
        return res
