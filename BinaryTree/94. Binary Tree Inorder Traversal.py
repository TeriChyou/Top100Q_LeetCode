from typing import List
from typing import Optional
# 2026 05 19
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
            if root is not None:
                self.dfs(root.left, res)
                res.append(root.val)
                self.dfs(root.right, res)
    
sol = Solution()
# Test Cases with Tree Nodes
node1 = TreeNode(1)
node1.left = None
node1.right = TreeNode(2)
node1.right.left = TreeNode(3)
print(sol.inorderTraversal(node1))
# 1 3 2
node2 = TreeNode(1)
node2.left = TreeNode(2)
node2.right = TreeNode(3)
node2.left.left = TreeNode(4)
node2.left.right = TreeNode(5)
node2.left.right.left = TreeNode(6)
node2.left.right.right = TreeNode(7)
node2.right.right = TreeNode(8)
node2.right.right.left = TreeNode(9)
print(sol.inorderTraversal(node2))
# 4 2 6 5 7 1 3 9 8
node3 = None
print(sol.inorderTraversal(node3))
# []
node4 = TreeNode(1)
print(sol.inorderTraversal(node4))
# [1]

"""
Stack, Tree, Depth-First Search, Binary Tree

The pattern is always: left subtree → current node → right subtree
"""