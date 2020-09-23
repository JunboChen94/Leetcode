class Solution:
    '''
    do not use additional instance variable
    '''
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _, ret = self.helper(root)
        return ret
        
    def helper(self, root: TreeNode) -> List[int]:
        if not root:
            return 0, 0
        left_nodes, left_max = self.helper(root.left)
        right_nodes, right_max = self.helper(root.right)
        return max(left_nodes + 1, right_nodes + 1), max([left_max, right_max, left_nodes + right_nodes])

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        def depth(root: TreeNode) -> int:
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            self.max = max(self.max, left + right)
            return max(left, right) + 1
        
        depth(root)
        return self.max
