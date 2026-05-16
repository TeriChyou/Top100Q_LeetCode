# 20260515
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        if target < min(candidates):
            return []
        """        
        result = []
        def combRecursion(index, curr, curr_comb):
            # prevent infinite index push
            if index == len(candidates):
                return
            # if curr sum == target, that's what we want
            if curr == target:
                result.append(curr_comb)
                return
            # if curr > target then terminate this branch.
            if curr > target:
                return
            # use the func twice:
            # stay at the same index, then add the curr candidate.
            combRecursion(index, curr+candidates[index], curr_comb + [candidates[index]])
            # skip the curr index, so don't add the curr candidate.
            combRecursion(index+1, curr, curr_comb)
            
        
        combRecursion(0, 0, [])
        
        return result
    

"""
When to push index? => By default or When the current num can not make target.
"""

class BetterSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def combRecursion(index, curr, curr_comb):
            # prevent infinite index push
            if index == len(candidates):
                return
            # if curr sum == target, that's what we want
            if curr == target:
                result.append(curr_comb)
                return
            # judge if the sum is larger than target          
            if curr+candidates[index] > target:
                return
            else:
                # skip the curr index, so don't add the curr candidate.
                combRecursion(index+1, curr, curr_comb)
                # stay at the same index, then add the curr candidate.
                combRecursion(index, curr+candidates[index], curr_comb + [candidates[index]])
            
        combRecursion(0, 0, [])
        
        return result



# 20260516 => review passed.
class ReviewSol:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []

        def cbRecusion(index, curr, curr_comb):
            if index==len(candidates):
                return
            if curr==target:
                res.append(curr_comb)
                return
            if curr>target:
                return
            else:
                cbRecusion(index, curr + candidates[index], curr_comb+[candidates[index]])
                cbRecusion(index+1, curr, curr_comb)
                
        
        cbRecusion(0, 0, [])

        return res
    
sol = ReviewSol()
print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2,3,5], 8))
print(sol.combinationSum([2], 1))