# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        '''
        Some algorithm in discussion traverse the whole tree, accumulate value
        if value is in range
        Here i explore the order info of BST, to save some time
        '''
        q = deque([root])
        ret = 0
        while len(q):
            node = q.popleft()
            if not node:
                continue
            if node.val < L:
                q.append(node.right)
            elif node.val > R:
                q.append(node.left)
            else:
                q.append(node.left)
                q.append(node.right)
                ret += node.val
        return ret
