class Solution:
'''
simple reservoir sampling, K=1
'''
def __init__(self, nums: List[int]):
    self.nums = nums

def pick(self, target: int) -> int:
    ret, count = None, 0
    for i, num in enumerate(self.nums):
        if not (num == target):
            continue
        count += 1
        if random.randint(1, count) == 1:
            ret = i
    return ret
