# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    level order traversal
    '''
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        g = defaultdict(list)
        queue = [(root, 0)]
        while root and queue:
            new = []
            d = defaultdict(list)
            for node, x in queue:
                d[x].append(node.val)
                if node.left:
                    new.append((node.left, x-1))
                if node.right:
                    new.append((node.right, x+1))
            for i in d:
                g[i].extend(sorted(d[i]))
            queue = new
        return [g[i] for i in sorted(g)]
            
            
                
        
