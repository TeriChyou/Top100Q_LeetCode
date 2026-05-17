# 20260517
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        res = [-1, -1]
        if n == 0:
            return res
        
        # divide and conquer, find left then find right
        def FindLeft():
            left, right = 0, n - 1
            leftmost = -1
            # Find leftmost
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    leftmost = mid
                    right = mid -1
            return leftmost
                    
        def FindRight():
            left, right = 0, n - 1
            rightmost = -1
            # Find mid
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    rightmost = mid
                    left = mid + 1
            return rightmost
        
        left = FindLeft()
        if left == -1:
            return res
        right = FindRight()        
        
        return [left, right]

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 0))
print(sol.searchRange([],42))
print(sol.searchRange([7,8,8,8,8,8,8,8,8,8,8,9],7))
print(sol.searchRange([7,8,8,8,8,8,8,8,8,8,8,9],8))
print(sol.searchRange([7,8,8,8,8,8,8,8,8,8,8,9],10))
print(sol.searchRange([1,2,2,2,2,3,4,5,5,5,5,6,7,8,9,10,11,12,12,12,12,12,13],2))
print(sol.searchRange([-999985131,-999953607,-999953607,-999915742,-999883817,-999849817,-999822901,-999815377,-999810801,-68594,-49967,20394,114012,999969829,999973689,999975494], -999953607))