# 20260515
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def gpRecursion(curr_open, curr_close, curr):
            if len(curr) == 2 * n:
                result.append(curr)
                return
            if curr_open < n:
                gpRecursion(curr_open + 1, curr_close, curr + '(')
            if curr_close < curr_open:
                gpRecursion(curr_open, curr_close + 1, curr + ')')
            
        gpRecursion(0,0,"")
            
        return result
    



"""
# When can we add an opening parenthesis '('?
- When the number of '(' used so far is less than n
# When can we add a closing parenthesis ')'? 
- When the number of ')' used so far is less than the number of '(' used
# What are the base cases for our recursion?
- When the current string length equals 2*n   

Time complexity: 4^n/n^(1/2) => Catalan number 卡塔蘭數
"""
# 20260516 => Review Passed.
class ReviewSol:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gpRecursion(open_num, close_num,curr,index):
            if index == 2*n:
                res.append(curr)
                return
            if open_num < n:
                gpRecursion(open_num + 1, close_num, curr + "(", index + 1)
            if close_num < open_num:
                gpRecursion(open_num, close_num+1, curr+")", index+1)
            
        gpRecursion(0,0,"",0)

        return res
    

# 1 <= n <= 8
sol = ReviewSol()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(1))