# 2026 05 21
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Since this used recursion stack thus space complexity is O(N)     
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.bfs(root)
        
        print(self.preorderTraversal(root))

    def bfs(self, root):
        if not root:
            return None
        
        if not root.left and root.right:
            return root
        
        # Run bfs at first
        leftTail = self.flatten(root.left)
        rightTail = self.flatten(root.left)
        
        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
            
        return rightTail if rightTail else leftTail
    
    # Just for checking   
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if root is not None:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)    
            
"""
Find rightmost node for each node's right node which doesn't has further right node.
See further explaination at editorial on leetcode.
"""
class MorrisTraversal:
    def flatten(self, root: Optional[TreeNode]) -> None: 
        if not root:
            return None
        
        node = root
        while node:
            # If there's left child
            if node.left:    
                rightmost = node.left
                # Find rightmost node for each node's right node which doesn't has further right node.
                while rightmost.right:
                    rightmost = rightmost.right
                    
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            # move on to the right side of the tree (which means that it's a new tree with left and right to do the Morris Traversal)
            node = node.right
sol = Solution()
# Also construct with preorder
root_1 = TreeNode(1)
root_1.left = TreeNode(2)
root_1.left.left = TreeNode(3)
root_1.left.right = TreeNode(4)
root_1.right = TreeNode(5)
root_1.right.right = TreeNode(6)

sol.flatten(root_1)



"""
Basically from inorder to preorder
Inorder: Left Mid Right
Preorder: Mid Left Right
And for preorder, root must be first number.
1. Deconstruct inorder.
2. Put them into list with Preorder.
3. Put back to the tree.
or
1. Simply modify the inorder tree to the preorder tree. (Since this is O(1))
Since:
In the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""