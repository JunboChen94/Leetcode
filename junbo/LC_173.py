# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    '''
    Based on inorder
    '''
    def __init__(self, root: TreeNode):
        self.stack = []
        self.root = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        node = self.stack.pop()
        self.root = node.right
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.root or self.stack
    '''
    Based on inorder, other slightly different version
    '''
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.pushAll(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack

    def pushAll(self, root: TreeNode):
        while root:
            self.stack.append(root)
            root = root.left
