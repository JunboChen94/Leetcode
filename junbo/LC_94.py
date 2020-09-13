# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        1) Create an empty stack S.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then
             a) Pop the top item from stack.
             b) Print the popped item, set current = popped_item->right
             c) Go to step 3.
        5) If current is NULL and stack is empty then we are done.
        '''
        stack = []
        ret = []
        current = root
        while current or len(stack):
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                ret.append(node.val)
                current = node.right
        return ret
        '''
        recursive
        '''
        # recursively
        def inorderTraversal1(self, root):
            res = []
            self.helper(root, res)
            return res
            
        def helper(self, root, res):
            if root:
                self.helper(root.left, res)
                res.append(root.val)
                self.helper(root.right, res)
