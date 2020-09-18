
class Solution:
    '''
    simple reservoir sampling, K=1
    '''
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        ret, count = None, 0
        p = self.head
        while p:
            count += 1
            if random.randint(1, count) == 1:
                ret = p.val
            p = p.next
        return ret
