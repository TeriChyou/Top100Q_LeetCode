#20260516
class Solution:
    def permute(self, nums):
        res = []
        # Recursion functions
        def permuteRecursion(numbers, path):
            # if numbers are used up
            if not numbers:
                # append the list into the res list
                res.append(path)
                return
            # get the left length for numbers
            for i in range(len(numbers)):
                # numbers[:i] means before current one, numbers[i+1:] means after the current one which means numbers - nubers[i]
                # then the path will be [] + [numbers[i]]
                permuteRecursion(numbers[:i] + numbers[i+1:], path + [numbers[i]])
        
        permuteRecursion(nums, [])
        
        return res    
    




# Time complexity
# O(n*n!)

class FasterSolution:
    def permute(self,nums):
        res = []
        
        if len(nums) == 1:
            # using : will be faster than 0?
            return [nums[:]]
        
        for _ in range(len(nums)):
            # why pop(0) works here? =>  rotation strategy [1,2,3] => [2,3] + [1] back => [3,1] + [2]
            num = nums.pop(0)
            # does this count as recursion here? => yes the second and the rest of recursions will have one less num since one of the num is popped off.
            permutations = self.permute(nums)
            # add the num popped out in perm then add to res?
            for perm in permutations:
                perm.append(num)
                res.append(perm)
            # idk the purpose of bring the popped num back. => [1,2,3] => [2,3] + [1] back => [3,1] + [2]
            nums.append(num)

        return res

sol = FasterSolution()


print(sol.permute([1, 2, 3]))
print(sol.permute([0, 1]))