class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    count += 1
                    self.search(grid, x, y)
        return count
        
    def search(self, grid: List[List[str]], x, y):
        if x< 0 or y < 0 or x >= len(grid) or y>= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        self.search(grid, x+1, y)
        self.search(grid, x, y+1)
        self.search(grid, x-1, y)
        self.search(grid, x, y-1)
