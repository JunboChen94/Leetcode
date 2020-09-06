class Solution:
def productExceptSelf(self, nums: List[int]) -> List[int]:
    '''
    Question: why a) and b) have about similar memory usage, but b) cost more memory dispite it does not generate any extra array?
    '''
    '''
    a)My initial solution, but memory should be optimized: 20.5MB
    '''
    product_prefix = list(accumulate([1] + nums, operator.mul))
    product_suffix = list(accumulate([1] + nums[::-1], operator.mul))[::-1]
    for i in range(0, len(nums)):
        nums[i] = product_prefix[i] * product_suffix[i+1]
    return nums
    
    '''
    b) my inplace solution: 21.7MB
    '''
    ret = nums[::-1]
    
    for i in range(1, len(ret)):
        nums[i] = nums[i] * nums[i-1]
        ret[i] = ret[i] * ret[i-1]
    
    l, r = 0, len(ret) -1
    while l < r:
        ret[l], ret[r] = ret[r], ret[l]
        l += 1
        r -= 1
    
    for i in range(len(ret) - 1, -1, -1):
        nums[i] = ret[i]
        ret[i] = (nums[i-1] if i - 1 >= 0 else 1) * (nums[i+1] if i + 1 < len(nums) else 1)
    
    return ret
    
    '''
    c) inplace solution in discussion session: 20.4MB,
       we do not need suffix array, we can use integer on the run since we do not need memory for backsequential  access
       we only need backsequential  access for one side
       
    '''
    p = 1
    n = len(nums)
    output = []
    for i in range(0,n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output
    
    '''
    use the following
    '''
    ret = list(accumulate([1]+nums, operator.mul))[:-1]
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        ret[i] = ret[i] * right
        right *= nums[i]
    return ret
    
