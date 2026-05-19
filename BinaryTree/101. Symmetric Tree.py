# 2026 05 19
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return []
        res = []
        self.dfs(root, res, None)
        n = (len(res) - 1) // 2
        left, right =  res[0:n], res[n+1:(len(res))][::-1]
        print(res)
        return left == right
    
    def dfs(self, root, res, prev):
            if root is not None:
                self.dfs(root.left, res, root)
                res.append(root.val)
                self.dfs(root.right, res, root)
            else:
                if prev is not None:
                    if prev.left is not None or prev.right is not None:
                        res.append(None)
    


"""
Key insight: A tree is symmetric if its left subtree is a mirror reflection of its right subtree. This requires comparing nodes in this pattern:

left.left ↔ right.right
left.right ↔ right.left
Instead of flattening the entire tree, try this recursive approach:

Create a helper function that takes two nodes (left and right)
Base cases:
If both are None → symmetric
If one is None but not the other → not symmetric
Recursive check:
Values must match
left.left must mirror right.right
left.right must mirror right.left
"""
# Editorial Solution
class EditorialSolution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        # if both are None
        if t1 is None and t2 is None:
            return True
        # if one of them are None but other one is not
        if t1 is None or t2 is None:
            return False
        
        return (
            # if left == symmetric right
            (t1.val == t2.val)
            # since we have to check all nodes
            # check this node's right and symmetric left
            and self.isMirror(t1.right, t2.left)
            # check this node's left and symmetric right
            and self.isMirror(t1.left, t2.right)
        )
# Python Cheat?
from collections import deque
class FasterSolution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # BFS
        
        if not root.left and not root.right:
            return True

        left_q = deque([root.left])
        right_q = deque([root.right])
            
        while left_q and right_q:
            level_size = len(left_q)
            if level_size != len(right_q):
                return False

            left_vals = []
            right_vals = []
            for _ in range(level_size):
                left_val = left_q.popleft()
                if left_val is not None:
                    left_vals.append(left_val.val)
                    left_q.append(left_val.left)
                    left_q.append(left_val.right)
                else:
                    left_vals.append('NULL')

                right_val = right_q.popleft()
                if right_val is not None:
                    right_vals.append(right_val.val)
                    right_q.append(right_val.left)
                    right_q.append(right_val.right)
                else:
                    right_vals.append('NULL')

            if left_vals != list(reversed(right_vals)):
                return False
        if left_q or right_q:
            return False
        return True
    
sol = FasterSolution()
# Tree 1
tree_1 = TreeNode(1)
tree_1.left = TreeNode(2)
tree_1.left.left = TreeNode(3)
tree_1.left.right = TreeNode(4)
tree_1.right = TreeNode(2)
tree_1.right.left = TreeNode(4)
tree_1.right.right = TreeNode(3)
# Tree 2
tree_2 = TreeNode(1)
tree_2.left = TreeNode(2)
tree_2.left.right = TreeNode(3)
tree_2.right = TreeNode(2)
tree_2.right.right = TreeNode(3)
# Tree 3 (Trivial)
tree_3 = TreeNode(1)
tree_3.left = TreeNode(2)
tree_3.right = TreeNode(2)
tree_3.left.left = TreeNode(2)
tree_3.right.left = TreeNode(2)
# Tree 4 (More Trivial)
tree_4 = TreeNode(5)
tree_4.left = TreeNode(2)
tree_4.right = TreeNode(2)
# Left child (index 1) has left child only
tree_4.left.left = TreeNode(4)
# Right child (index 2) has right child only
tree_4.right.right = TreeNode(1)
# Node 4 (index 3) has right child only
tree_4.left.left.right = TreeNode(1)
# Node 1 (index 6) has both children
tree_4.right.right.left = TreeNode(4)
tree_4.right.right.right = TreeNode(2)
# Node 1 (index 8) has right child only
tree_4.left.left.right.right = TreeNode(2)

print(sol.isSymmetric(tree_1))
print(sol.isSymmetric(tree_2))
print(sol.isSymmetric(tree_3))
print(sol.isSymmetric(tree_4))

"""
    Original (DFS Flatten)	                        BFS Solution
Flattens entire tree into 1D array	        Processes level-by-level
Loses parent-child hierarchy	            Preserves level structure
Compares array halves	                    Compares mirrored levels
Fails on structural asymmetry	            Catches structural asymmetry
"""