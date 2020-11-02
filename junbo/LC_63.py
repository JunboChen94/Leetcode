class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Previous no obstacle, no need to do DP, since only m-1 and n-1 down and right
        are needed. which is C (m+n-2) (m-1)
        '''
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # initalize steps of first row
        steps = itertools.accumulate(obstacleGrid[0], lambda x,y: x or y)
        steps = [1 - i for i in steps]
        for i in range(1, m):
            temp = [1-i for i in obstacleGrid[i]]
            temp[0] = temp[0] and steps[0]
            for j in range(1, n):
                temp[j] = 0 if not temp[j] else temp[j-1] + steps[j]
            steps = temp
        return steps[-1]
