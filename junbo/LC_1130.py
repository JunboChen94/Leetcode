class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        # T = O(n^2), M = O(n)
        # res = 0
        # while len(A) > 1:
        #     # delete a from smallest to largest
        #     i = A.index(min(A))
        #     # use smaller b to delete a
        #     res += min(A[i-1:i]+A[i+1:i+2]) * A.pop(i)
        # return res
        
        # Stack: T = O(n), M=O(n)
        res = 0
        # stack's elements are in descending order
        stack = [float(inf)]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res 
