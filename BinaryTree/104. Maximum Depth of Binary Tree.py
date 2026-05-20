# 2026 05 20
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: # This one is BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = []
        def bfs(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                bfs(node.left, level+1)
            if node.right:
                bfs(node.right, level+1)
        
        bfs(root, 0)
        
        return len(res)

class DFSSolution: # Simpler
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            l_h = self.maxDepth(root.left)
            r_h = self.maxDepth(root.right)
            return max(l_h, r_h) + 1 # since it's zero-indexed

sol = Solution()
# tree 1
tree_1 = TreeNode(3)
tree_1.left = TreeNode(9)
tree_1.right = TreeNode(20)
tree_1.right.left = TreeNode(15)
tree_1.right.right = TreeNode(7)

# tree 2
tree_2 = TreeNode(1)
tree_2.right = TreeNode(2)

print(sol.maxDepth(tree_1))
print(sol.maxDepth(tree_2))



"""
First solution is just 102's copy but to show it's len.
Second solution is using DFS to get the length.
"""