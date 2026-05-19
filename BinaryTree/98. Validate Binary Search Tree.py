# 2026 05 19
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev = float('-inf')
        
        def inorder(node):
            nonlocal prev # let prev able to be modified.
            # This is just first check if prev valid and curr no node then must be true.
            if not node:
                return True
            # Left (if left tree doesn't exist and prev < current node then => True and True => False)
            if not (inorder(node.left) and prev < node.val):
                return False
            # Prev
            prev = node.val
            # Right
            return inorder(node.right)
        
        return inorder(root)


sol = Solution()
# true
tree1 = TreeNode(2)
tree1.left = TreeNode(1)
tree1.right = TreeNode(3)
print(sol.isValidBST(tree1))
# false
tree2 = TreeNode(5)
tree2.left = TreeNode(1)
tree2.right = TreeNode(4)
tree2.right.left = TreeNode(3)
tree2.right.right = TreeNode(6)
print(sol.isValidBST(tree2))


"""
A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

class BetterUnderstandingSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            # if current val < low or > high then it's violated 
            if not (low < node.val < high):
                return False
            
            # since any branch is false then it's eventually false
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))