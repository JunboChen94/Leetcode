class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        shortest path in a unweighted graph. BFS. It is not tree, so we need dict to record visited node
        '''
        dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
        dys = [-1, 1, -2, 2, -2, 2, -1, 1]
        nodes = [(0, 0)]
        visited, steps =set(), 0
        visited.add((0,0))
        while nodes and (x,y) not in visited:
            temp = []
            for node in nodes:
                for dx, dy in zip(dxs, dys):
                    new_node = (node[0]+dx, node[1]+dy)
                    if new_node in visited:
                        continue
                    visited.add(new_node)
                    temp.append(new_node)
            steps += 1
            nodes = temp
        return steps
        
        '''
        To decrease the searching space by greedy first
        And since the checker board is inf
        we do not care the sign
        '''
        '''
        shortest path in a unweighted graph. BFS. It is not tree, so we need dict to record visited node
        '''
        '''
        Use greedy to decrease the search space
        '''
        x, y = abs(x), abs(y)
        res = 0
        while x > 4 or y > 4:
            if x > y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                y -= 2
                x -= 1 if x >= 1 else -1
            res += 1
        '''
        Use BFS to search
        '''
        queue = collections.deque([(0,0)])
        d = {(0,0):0}
        while queue:
            node = queue.popleft()
            if node == (x, y):
                return d[node] + res
            for dx, dy in zip([-1,-1,1,1,-2,-2,2,2], [-2,2,-2,2,-1,1,-1,1]):
                new_node = (node[0]+dx, node[1]+dy)
                if new_node not in d:
                    d[new_node] = d[node] + 1
                    queue.append(new_node)
        return -1
        
