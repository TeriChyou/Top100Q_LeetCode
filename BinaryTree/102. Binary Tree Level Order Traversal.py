# 2026 05 20
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
             
        left_q = deque([root.left])
        right_q = deque([root.right])
        
        res = [[root.val]]
        l_res = []
        r_res = []
        while left_q:
            level_size = len(left_q)
            left_vals = []
            for _ in range(level_size):
                left_val = left_q.popleft()
                if left_val is not None:
                    left_vals.append(left_val.val)
                    left_q.append(left_val.left)
                    left_q.append(left_val.right)
            if left_vals != []:
                l_res.append(left_vals)
            
        while right_q:
            level_size = len(right_q)
            right_vals = []
            for _ in range(level_size):
                right_val = right_q.popleft()
                if right_val is not None:
                    right_vals.append(right_val.val)
                    right_q.append(right_val.left)
                    right_q.append(right_val.right)
            if right_vals != []:
                r_res.append(right_vals)
        min_len = 0
        selected = "l"
        if len(l_res) > len(r_res):
            min_len = len(r_res)
            selected = "l"
        elif len(l_res) < len(r_res):
            min_len = len(l_res)
            selected = "r"
        else:
            min_len = len(l_res)
            selected = "l"
            
        for i in range(min_len):
            if selected == "l":
                l_res[i] += r_res[i]
            else:
                r_res[i] = l_res[i] + r_res[i]

        if selected == "l":
            return res + l_res
        else:
            return res + r_res
        


"""
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
Hint: Use a queue to perform BFS.

Since my first approach is long and have unecessary stuffs like more variables and could be slower than BFS, 
BFS is still better.
"""

class RecursionSolution: # <- Recommended
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        def bfs(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                bfs(node.left, level+1)
            if node.right:
                bfs(node.right, level+1)
        
        bfs(root, 0)
        
        return res

class IterationSolution: # <- Recommended
    def levelOrder(self, root):
        if not root: return []
        q, res = deque([root]), []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res

sol = Solution()

# tree_1
tree_1 = TreeNode(3)
tree_1.left = TreeNode(9)
tree_1.right = TreeNode(20)
tree_1.right.left = TreeNode(15)
tree_1.right.right = TreeNode(7)

# tree_2
tree_2 = TreeNode(1)

# tree_3
tree_3 = None

# tree_4
tree_4 = TreeNode(1)
tree_4.left = TreeNode(2)
tree_4.left.left = TreeNode(3)
tree_4.left.left.left = TreeNode(4)
tree_4.left.left.left.left = TreeNode(5)

print(sol.levelOrder(tree_1))
print(sol.levelOrder(tree_2))
print(sol.levelOrder(tree_3))
print(sol.levelOrder(tree_4))