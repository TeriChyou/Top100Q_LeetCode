# 2026 05 22
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Recursive Inorder Traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(r: Optional[TreeNode]) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]

# Iterative Inorder Traversal => Faster
class OtherSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
    
sol = Solution()
# tree_1
tree_1 = TreeNode(3)
tree_1.left = TreeNode(1)
tree_1.left.right = TreeNode(2)
tree_1.right = TreeNode(4)

# tree_2
tree_2 = TreeNode(5)
tree_2.left = TreeNode(3)
tree_2.left.left = TreeNode(2)
tree_2.left.left.left = TreeNode(1)
tree_2.left.right = TreeNode(4)
tree_2.right = TreeNode(6)

print(sol.kthSmallest(tree_1, 1))
print(sol.kthSmallest(tree_2, 3))