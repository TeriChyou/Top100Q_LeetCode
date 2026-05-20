# 2026 05 20
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Initialize the Mapping:
        # Create a dictionary mapping to store the index of each value from the inorder list.
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        """
        The preorder list is converted into a deque. 
        A deque (double-ended queue) allows efficient popping of elements from the front, 
        which is crucial because the algorithm needs to pop the next root node from the preorder list in each recursive call.
        """
        preorder = deque(preorder)
        
        def build(start, end):
            # If the current range is invalid (i.e., the start index exceeds the end index), return None. 
            # This indicates no subtree exists for this range.
            if start > end:
                return None
            # Create a new TreeNode using the next value from the preorder deque, 
            # which represents the root of the current subtree.
            root = TreeNode(preorder.popleft())
            # Use the mapping dictionary to find the index of the root value in the inorder list. 
            # This index helps in dividing the inorder list into left and right subtrees.
            mid = mapping[root.val]
            # Recursively build the left subtree using the range from start to mid - 1 in the inorder list.
            root.left = build(start, mid - 1)
            # Recursively build the right subtree using the range from mid + 1 to end in the inorder list.
            root.right = build(mid + 1, end)
            
            # Since root got recursively returned, it's well constructed at the end of the function.
            return root
        
        return build(0, len(preorder) - 1)
    
class SlowerSolution: # O(n^2)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        The preorder list is converted into a deque. 
        A deque (double-ended queue) allows efficient popping of elements from the front, 
        which is crucial because the algorithm needs to pop the next root node from the preorder list in each recursive call.
        """
        preorder = deque(preorder)
        """
        preorder: A deque containing the remaining nodes to be processed in preorder.
        inorder: A list representing the current subtree's inorder traversal.
        """
        def build(preorder, inorder):
            # if the inorder list is not empty
            if inorder:
                """
                The next root node is obtained by popping the leftmost element from preorder (using popleft()). 
                The index of this root node is then found in the inorder list using the index() function.
                The idx represents the position of the root node in the inorder list,
                which helps in dividing the list into left and right subtrees.
                """
                idx = inorder.index(preorder.popleft())
                # A new TreeNode is created with the value inorder[idx]. This node will be the root of the current subtree being processed.
                root = TreeNode(inorder[idx]) 
                # Recursively Build the Left and Right Subtree
                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx+1:])

                return root

        return build(preorder, inorder)

class MuchFasterSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)
"""
Pre: 
print root.val
trav(root.left)
trav(root.right)

in
trav(root.left)
print root.val
trav(root.right)



root is always pre[0]
right bottom is always pre[-1] and in[-1]
"""

sol = Solution()
# [3,9,20,null,null,15,7]
print(sol.buildTree([3,9,20,15,7],[9,3,15,20,7]))
# [-1]
print(sol.buildTree([-1], [-1]))


"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Inorder: Left Mid Right
Preorder: Mid Left Right


"""