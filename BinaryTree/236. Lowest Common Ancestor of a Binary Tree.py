# 2026 05 22
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Approach
class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(current_node: TreeNode) -> bool:

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
    
# Iterative using parent pointers => Slower
class OtherSolution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

# Recursive

class FastSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right) or (root is p) or (root is q):
            return root

        return left or right

def list_to_tree(elements):
    if not elements:
        return None
    
    root = TreeNode(elements[0])
    queue = [root]
    i = 1
    
    while queue and i < len(elements):
        curr = queue.pop(0)
        
        # Assign left child
        if elements[i] is not None:
            curr.left = TreeNode(elements[i])
            queue.append(curr.left)
        i += 1
        
        # Assign right child
        if i < len(elements) and elements[i] is not None:
            curr.right = TreeNode(elements[i])
            queue.append(curr.right)
        i += 1
        
    return root

sol = Solution()
print(sol.lowestCommonAncestor(list_to_tree([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(1)))
print(sol.lowestCommonAncestor(list_to_tree([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(4)))