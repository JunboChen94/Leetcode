class Solution:

    def __init__(self, w: List[int]):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))
