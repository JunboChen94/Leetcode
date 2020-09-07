# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        use iterative BFS with queue
        '''
        ret = []
        if not root:
            return ret
        queue = deque([(root, 0)])
        while len(queue):
            node, plevel = queue.popleft()
            if len(ret) == plevel:
                ret.append([node.val])
            else:
                ret[plevel].append(node.val)
            if node.left:
                queue.append((node.left, plevel + 1))
            if node.right:
                queue.append((node.right, plevel + 1))
        return ret
        
        '''
        We can also implement it not using plevel, but with nested list
        '''
        ret = []
        if not root:
            return ret
        q = deque([root])
        while len(q):
            ret.append([x.val for x in q])
            temp = deque([])
            while len(q):
                node = q.popleft() # somebody use pop(0), which is O(n), use deque
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
        return ret
        '''
        Without using queue
        '''
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRs = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRs for leaf in LR if leaf]
        return ans 
        
