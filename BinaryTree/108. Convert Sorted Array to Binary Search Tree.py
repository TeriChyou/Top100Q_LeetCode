# 2026 05 21
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Initialize the Mapping:
        # Create a dictionary mapping to store the index of each value from the inorder list.
        mapping = {}
        for i in range(len(nums)):
            mapping[nums[i]] = i
        
        def build(start, end):
            
            if start > end:
                return None
            
            mid = (start + end) // 2
            
            root = TreeNode(nums[mid])
            
            root.left = build(start, mid - 1)
            
            root.right = build(mid + 1, end)
        
            return root
        
        return build(0, len(nums) - 1)
    
sol = Solution()   
#
print(sol.sortedArrayToBST([-10, -3, 0 ,5 ,9]))
print(sol.sortedArrayToBST([1, 3]))
print(sol.sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
    
"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.


1. If the array is empty, return null.
2. Find the middle element of the array and create a new node with its value.
3. Recursively construct the left subtree using the left half of the array.
4. Recursively construct the right subtree using the right half of the array.
5. Set the left and right child of the node created in step 2 to the root of the left and right subtree respectively.
6. Return the root node.

Credit: Amit Mungare

Similar concept to Question 105, it's the pre-quest for 105
"""

