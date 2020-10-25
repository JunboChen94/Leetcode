class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        left = [interval for interval in intervals if interval[1] < s]
        right = [interval for interval in intervals if interval[0] > e]
        if left + right != intervals:
            s = min(intervals[len(left)][0], s)
            e = max(intervals[~len(right)][1], e)
        return left + [[s, e]] + right
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        parts = merge, left, right = [], [], []
        for i in intervals:
            parts[(i[1] < s) - (i[0] > e)].append(i)
        if merge:
            s = min(merge[0][0], s)
            e = max(merge[-1][1], e)
        return left + [[s,e]] + right
        
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left.append(i)
            elif i[0] > e:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s,e]] + right
