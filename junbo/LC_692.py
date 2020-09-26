class Solution:
    '''
    In this question, rank count is large first, but key is small first
    O(nlogk) requirement is obvious sign to use heapq
    But do not use heapq.nlargest since we need n most frequent key. Since in this way we need to find my to reverse the comparator for alphabentical order for string, which is not possible
    But we can easily reverse count order by ~count or -count os large count first
    small alphabetic order is simple
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        table = defaultdict(int)
        for word in words:
            table[word] += 1
        return heapq.nsmallest(k, table, lambda x : (-table[x], x))
