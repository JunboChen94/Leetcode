# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    recursive solution
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret, stack = [], [root]
        while root and stack:
            node = stack.pop()
            ret.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ret[::-1]
    '''
    recursive solution
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        self.helper(root, ret)
        return ret
        
    def helper(self, root: TreeNode, ret: List[int]) -> List[int]:
        if root:
            self.helper(root.left, ret)
            self.helper(root.right, ret)
            ret.append(root.val)
