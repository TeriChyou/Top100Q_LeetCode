# 20260518
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # check if the method is correct
        while left < right:
            mid = (left + right) // 2
            # Minimum must be in the right half. (unsorted)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
            
        
    

sol = Solution()
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([11,13,15,17]))
print(sol.findMin([2,1]))

"""
You must write an algorithm that runs in O(log n) time.
"""