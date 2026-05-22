# 2026 05 22
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None   
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root    
    
sol = Solution()
# tree_1
tree_1 = TreeNode(4)
tree_1.left = TreeNode(2)
tree_1.left.left = TreeNode(1)
tree_1.left.right = TreeNode(3)
tree_1.right = TreeNode(7)
tree_1.right.left = TreeNode(6)
tree_1.right.right = TreeNode(9)



"""
a) Recursive Approach:

check whether the root is null or not..
go to the left most node of tree using RECURSION and store node.
go to the right most node of tree using RECURSION and store node.
swap both stored node.
return root
-- Time Complexity: O(n)
-- Space Complexity: O(n)

b) Iterative Approach:

create Queue
check whether the root is null or not.
add root to the queue.
loop until queue is not empty and then remove element from queue and store it. Then, check for left and right element and add to queue.
Finally, swap the element.
return root.
-- Time Complexity: O(n)
-- Space Complexity: O(n)
"""