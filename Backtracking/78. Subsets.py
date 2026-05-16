# 20260516 => passed without AI's instruction and aid.
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]
        
        nums.sort()
        
        res = [[]]
        
        # for loop
        for i in range(len(nums)):
            # CoT:recursion here to make the previous number's subset added onto the number itself.
            for j in range(len(res) - 1):
                curr = [nums[i]] + res[j+1]
                res.append(curr)
            # add its own set
            res.append([nums[i]])
 
        return res
    


sol = Solution()
print(sol.subsets([1,2,3]))
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(sol.subsets([0]))
# [[],[0]]

"""
The solution set must not contain duplicate subsets. Return the solution in any order.
1. need an empty set
2. No duplicated (Must not use if...in...)
3. recursion here to make the previous number's subset added onto the number itself.
"""