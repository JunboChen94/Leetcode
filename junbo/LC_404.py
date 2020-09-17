class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        '''
        In order traversal
        '''
        if not root: return 0
        if root.left and (not root.left.left) and (not root.left.right):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
