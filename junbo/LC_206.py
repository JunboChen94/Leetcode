# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while head:
            prev = ListNode(head.val, prev)
            head = head.next
        return prev
