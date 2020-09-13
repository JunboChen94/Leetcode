# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    interative
    '''
    stack, ret = [], []
    while root or stack:
        if root:
            ret.append(root.val)
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            root = node.right
    return ret
    
    '''
    resurive
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        self.helper(root, ret)
        return ret
        
    def helper(self, root: TreeNode, ret: List[int]) -> List[int]:
        if root:
            ret.append(root.val)
            self.helper(root.left, ret)
            self.helper(root.right, ret)
