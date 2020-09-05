class Solution:
def subarraySum(self, nums: List[int], k: int) -> int:
    '''
    Happy to figure out this solution step by step
    First sum of all combination of substring can be be calculated with
    itertools.accumulate([0] + nums), sunij = T[j] - T[i]
    Then since T[j] - T[i] = k, the problem suddenly becomes two sum
    Howeever, in two sum there is no duplicate numver, here we have
    ex: nums = [1,0,0,0,6], accus = [0, 1,1,1,1,7]
    so we can use hashmap, count number of occurrance.
    Keep praticing, programming is fun and an important cornertone for research. 
    '''
    acums = list(itertools.accumulate([0] + nums))
    T = {}
    ret = 0
    for acum in acums:
        if acum - k in T:
            ret += T[acum - k]
        if acum in T:
            T[acum] += 1
        else:
            T[acum] = 1
    return ret
