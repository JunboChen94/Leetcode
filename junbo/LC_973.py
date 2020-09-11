class Solution:
def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    '''
    Here point[0] ** 2 + point[1] ** 2 could be really huge, leverage python
    assign bytes to int based on variable value, so it won't overflow.
    O(nlogn)
    '''
    # new_points = sorted(points, key=lambda p: p[0]*p[0]+p[1]*p[1])
    # return new_points[:K]
    '''
    To make it faster, we can use max heap (priority queue), maintain a queue
    with size K.
    O(NlogK)
    Since min heap is using priority queue algorithm based on array
    here heapq is not data structure but algorithm to maintain min-heap
    property for list
    '''
    heap = []
    for i, point in enumerate(points):
        dist = - (point[0]**2 + point[1]**2)
        if len(heap) == K:
            heapq.heappushpop(heap, (dist, i))
        else:
            heapq.heappush(heap, (dist, i))
    return [points[i] for _, i in heap]
    '''
    Quick SelectL T(n) = T(n/2) + O(n), O(n)
    '''
    '''
    Use quick-select, T(n) = (T/2) + O(n), so it is O(n)
    '''
    def partition(points, left, right):
        pivot_dist = points[right][0]**2 + points[right][1]**2
        p = left
        for q in range(left, right):
            if points[q][0]**2 + points[q][1]**2 <= pivot_dist:
                points[p], points[q] = points[q], points[p]
                p += 1
        points[p], points[right] = points[right], points[p]
        return p
    
    left, right = 0, len(points) - 1
    while left < right:
        mid = partition(points, left, right)
        if mid == K:
            break
        elif mid > K:
            right = mid - 1
        else:
            left = mid + 1
    return points[:K]
    
    '''
    recursive
    '''
    class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        Use quick-select, T(n) = (T/2) + O(n), so it is O(n)
        '''
        self.sort(points, 0, len(points) - 1, K)
        return points[:K]
    
    
    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p+1, r, K)
            else:
                self.sort(points, l, p-1, K)
    
    def partition(self, points, left, right):
        index = random.randint(left, right)
        points[index], points[right] = points[right], points[index]
        pivot_dist = points[right][0]**2 + points[right][1]**2
        p = left
        for q in range(left, right):
            if points[q][0]**2 + points[q][1]**2 <= pivot_dist:
                points[p], points[q] = points[q], points[p]
                p += 1
        points[p], points[right] = points[right], points[p]
        return p
    
