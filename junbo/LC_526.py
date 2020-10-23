class Solution:
    '''
    It is backtracing solution
    '''
    def countArrangement(self, N: int) -> int:
        self.N = N
        self.ret = 0
        self.used = [0] * N
        self.visit(1)
        return self.ret


    def visit(self, index: int):
        if index == self.N + 1:
            self.ret += 1
            return
        for i in range(1, self.N+1):
            if self.used[i-1] or 0 not in [i%index, index%i]:
                continue
            self.used[i-1] = 1
            self.visit(index+1)
            self.used[i-1] = 0
    
    def countArrangement(self, N: int) -> int:
        '''
        use Backtracing + DP
        aaaaac1c2c3d1d2d3
        when perumate c1, c2, c3, they all need d1,d2,d3
        no need to calculate again
        '''
        cache = {}
        def helper(X):
            if len(X) == 1:
                # since i = 1, any digit is divisible by 1
                return 1
            if X in cache:
                return cache[X]
            total = sum(helper(X[:j]+X[j+1:])
                        for j, x in enumerate(X)
                        if len(X)%x == 0 or x%len(X)==0)
            cache[X] = total
            return total
        return helper(tuple(range(1,N+1)))
            
