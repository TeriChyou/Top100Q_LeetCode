from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        result = []
        # make a digit map at first
        digit_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        # Use backtracking as the main method to make combinations
        def backtracking(curr_combination, index):
            if index == len(digits):
                result.append(curr_combination)
                return # remember to return it's really important.
            for i in digit_map[digits[index]]:
                backtracking(curr_combination + i, index + 1)

        
        backtracking("", 0)

        return result


sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations("2"))

"""
Using backtracking as the main method to make combinations:
For example, for case "23"
then put it into backtracking, it will be like:
2:abc, 3:def, then it will process like this:
a[index 0]+d[index1] => return
a[index 0]+e[index1] => return
a[index 0]+f[index1] => return
...
since recursion will automatically run till the index == len(digits)
that's why return in "backtracking" is important

O(4^n x n)
"""

class BetterSolution:
    def letterCombinations(self, digits: str) -> List[str]:
        # firstly make edge case with empty str
        if not digits:
            return []
        
        # then make a digit map => using digits instead of strings
        digit_map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        # then use for loops for iteration
        combinations = [""]
        # 1. run all digits
        for digit in digits:
            # start with empty comb.
            new_comb = []
            # 2. expand the comb, since the first comb is "" then it will be "" + a, "" + b, "" + c in 3. then back to 1.
            # thus it will be "a" + d, "a" + e, "a" + f...
            for comb in combinations:
                # 3. get each digit from map then put it into the string comb.
                for letter in digit_map[digit]:
                    new_comb.append(comb + letter)
            combinations = new_comb

        return combinations

# 20260516 => Review Failed with wrong algo in for loops
class ReviewSol:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dig_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u', 'v'],
            '9': ['w','x','y','z']
        }
        combinations = [""]
        # search every digits
        for digit in digits:
            curr_comb = [] # => every new comb is made here
            # search every letter that is put into the comb
            for comb in combinations:
                # put every letter after the first ""
                for letter in dig_map[digit]:
                    curr_comb.append(comb + letter)
                combinations = curr_comb
        
        return combinations
            
sol = ReviewSol()
print(sol.letterCombinations("23"))
print(sol.letterCombinations("2"))