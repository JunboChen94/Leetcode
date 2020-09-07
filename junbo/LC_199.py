# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    My solution based on LC_102: Binary Tree Level Order Traversal; Here I use
    level list, could be replace with queue
    '''
    def rightSideView(self, root: TreeNode) -> List[int]:
        ret, level = [], [root]
        while root and level:
            ret.append(level[-1].val)
            LRs = [(x.left, x.right) for x in level]
            level = [leaf for LR in LRs for leaf in LR if leaf]
        return ret
    
