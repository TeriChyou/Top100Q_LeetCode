# 2026 05 21
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        self.rightView(root, res, 0)
        return res
        
    def rightView(self, curr, res, depth):
        if curr is None:
            return
        
        # 
        if depth == len(res):
            res.append(curr.val)
        
        self.rightView(curr.right, res, depth + 1)
        self.rightView(curr.left, res, depth + 1)

class DequeSolution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        result=[]

        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()

                if i==size-1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
            
sol = Solution()
# tree_1 [1,3,4]
tree_1 = TreeNode(1)
tree_1.left = TreeNode(2)
tree_1.left.right = TreeNode(5)
tree_1.right = TreeNode(3)
tree_1.right.right = TreeNode(4)
# tree_2 [1,2,4,5]
tree_2 = TreeNode(1)
tree_2.left = TreeNode(2)
tree_2.right = TreeNode(3)
tree_2.left.left = TreeNode(4)
tree_2.left.left.left = TreeNode(5)
# tree_3 [1,3,6,4]
tree_3 = TreeNode(1)
tree_3.left = TreeNode(2)
tree_3.left.right = TreeNode(5)
tree_3.left.right.left = TreeNode(4)
tree_3.right = TreeNode(3)
tree_3.right.left = TreeNode(6)

print(sol.rightSideView(tree_1))
print(sol.rightSideView(tree_2))
print(sol.rightSideView(tree_3))

"""
BFS > DFS since it has to consider left and right simutaneously.
"""