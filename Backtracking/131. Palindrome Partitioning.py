# 20260517
from typing import List
# Original solution with  O(n × 2ⁿ × k) Time Complexity
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
           return [[s[:]]]
        # make a function to check
        def isPalindrome(testor):
            return testor[::-1] == testor
        res = []
        
        def backtracking(start, curr):
            # if reach the maximum then return final substring lists
            if start == len(s):
                res.append(curr[:])
                return
            # from start to end +1 to check each palindrome substrings
            for end in range(start, len(s)):
                substring = s[start:end+1]
                
                if isPalindrome(substring):
                    # if pal., then curr + substring
                    curr.append(substring)
                    # go to next recursion
                    backtracking(end+1, curr)
                    # then go back to previous state then keep the for loop going.
                    curr.pop()
            
        backtracking(0, [])
        return res
   
sol = Solution()
# output = [["a","a","b"],["aa","b"]]
print(sol.partition("aab"))
print("---------------")
# output = [["a"]]
print(sol.partition("a"))
print("---------------")
# output = [["a","b","c","a","a"],["a","b","c","aa"]]
print(sol.partition("abcaa"))
print("---------------")
# output = [["a","a","a","b"],["a","aa","b"],["aa","a","b"],["aaa","b"]]
print(sol.partition("aaab"))

"""
1 <= s.length <= 16
s contains only lowercase English letters.
# String
# Dynamic Programming
# Backtracking

CoT:
1. Make if it's valid palindrome function.
2. Using for loop for fixed maximum length of palindrome.
3. Get 1 item in s, then get 2, get 3...till reach maximum, and use check function to check then appened to curr_res.
4. at each position, try ALL possible palindromic substrings starting from that position, then recursively process what's left.
** When you choose a palindrome substring starting at index i with length L, where should the NEXT substring start? How can you track this in your algorithm?

pop() undoes the append(), and curr[:] creates a snapshot copy

"""
# Time Complexity: O(n² + n × 2ⁿ)
class BetterSolution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
           return [[s[:]]]
        
        n = len(s)
        # Precompute palindrome table: is_pal[i][j] = True if s[i:j+1] is palindrome
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True  # Single char is palindrome
        for i in range(n-1):
            is_pal[i][i+1] = (s[i] == s[i+1])  # Two chars palindrome if equal
        
        # Fill table for lengths >= 3: s[i:j] is palindrome if s[i]==s[j] and s[i+1:j-1] is palindrome
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
        
        res = []
        def backtracking(start, curr):
            if start == len(s):
                res.append(curr[:])
                return
            
            for end in range(start, len(s)):
                # O(1) palindrome check using precomputed table instead of O(k) string reversal
                if is_pal[start][end]:
                    curr.append(s[start:end+1])
                    backtracking(end+1, curr)
                    curr.pop()
            
        backtracking(0, [])
        return res
# Explanation by Leet
"""
is_pal[i][j] 代表：字串 s 從索引 i 到 j（包含）的子字串是否為回文

舉例：如果 s = "aab"，那麼：

is_pal[0][0] = True（"a" 是回文）
is_pal[0][1] = True（"aa" 是回文）
is_pal[1][2] = False（"ab" 不是回文）
--------------------------------------------------------------
第一步：初始化單字元（長度 = 1）
for i in range(n):
    is_pal[i][i] = True  # 任何單一字元都是回文
Apply Code
例子 s = "aab"（n=3）：

索引:
    [a]  [a]  [b]
     0    1    2
0  [ T ,  ? ,  ? ]
1  [ ? ,  T ,  ? ]
2  [ ? ,  ? ,  T ]  ← 對角線全為 True
--------------------------------------------------------------
第二步：處理雙字元（長度 = 2）
for i in range(n-1):
    is_pal[i][i+1] = (s[i] == s[i+1])
Apply Code
例子 s = "aab"：

is_pal[0][1]：s[0]='a' == s[1]='a' → True（"aa" 是回文）
is_pal[1][2]：s[1]='a' != s[2]='b' → False（"ab" 不是回文）
表格狀態：

     0    1    2
0  [ T ,  T ,  ? ]
1  [ ? ,  T ,  F ]
2  [ ? ,  ? ,  T ]
--------------------------------------------------------------
第三步：處理長度 ≥ 3 的情況（動態規劃核心）
for length in range(3, n+1):      # 從長度 3 開始
    for i in range(n - length + 1):
        j = i + length - 1
        is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
Apply Code
核心邏輯：

s[i:j+1] 是回文 當且僅當：

兩端字元相等：s[i] == s[j]
且中間部分也是回文：is_pal[i+1][j-1] == True
例子 s = "abcaa"（n=5），計算 is_pal[2][4]（即 "caa"）：

i=2, j=4, length=3
檢查：
1. s[2]='c' == s[4]='a'？→ False ❌
2. 不用檢查 is_pal[3][3]（因為第一步已失敗）
結果：is_pal[2][4] = False
另一例 s = "aabaa"，計算 is_pal[0][4]（即 "aabaa"）：

i=0, j=4, length=5
檢查：
1. s[0]='a' == s[4]='a'？→ True ✓
2. is_pal[1][3]（即 "aba"）是否為 True？
   → 需要先計算 is_pal[1][3]...
   → is_pal[1][3] 依賴 is_pal[2][2]（已知為 True）
   → 最終 is_pal[1][3] = True
結果：is_pal[0][4] = True（"aabaa" 是回文）
# Why?
動態規劃的優勢：

避免重複計算：原本每次都要用 substring[::-1] == substring 檢查（O(k) 時間）
記憶化：一旦計算過 is_pal[i][j]，後續直接查表（O(1) 時間）
由小到大建構：先算短的，再用短的結果算長的
時間複雜度對比：

原方法：每次檢查回文 O(k)，總共可能檢查 O(n × 2ⁿ) 次 → O(n × 2ⁿ × k)
優化後：預計算 O(n²) + 查表 O(1) × O(n × 2ⁿ) → O(n² + n × 2ⁿ)
"""

class ExplanationSolution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # Check if only one element
        if n == 1:
            return [[s[:]]]
        # Make Palindrome Table
        # Step.1 Make the table all false, take "aabaa" as example
        pal_table = [[False] * n for _ in range(n)] # here using false to explain
        # Step.2 Make all single char spot True
        for i in range(n):
            pal_table[i][i] = True
        """
            [a]  [a]  [b]  [a]  [a]
             0    1    2    3    4
         0 [ T ,  ? ,  ?  , ? ,  ? ]
         1 [ ? ,  T ,  ?  , ? ,  ? ]
         2 [ ? ,  ? ,  T  , ? ,  ? ]
         3 [ ? ,  ? ,  ?  , T ,  ? ]
         4 [ ? ,  ? ,  ?  , ? ,  T ] 
        """
        # Step.3 Check neighbor if pal.
        for i in range(n-1):
            pal_table[i][i+1] = (s[i] == s[i+1])
        """
            [a]  [a]  [b]  [a]  [a]
             0    1    2    3    4
         0 [ T ,  T ,  ?  , ? ,  ? ]
         1 [ ? ,  T ,  ?  , ? ,  ? ]
         2 [ ? ,  ? ,  T  , ? ,  ? ]
         3 [ ? ,  ? ,  ?  , T ,  T ]
         4 [ ? ,  ? ,  ?  , ? ,  T ] 
        """
        
        # Step.4 Handle length >= 3
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                pal_table[i][j] = (s[i] == s[j] and pal_table[i+1][j-1])
        """
            [a]  [a]  [b]  [a]  [a]
             0    1    2    3    4
         0 [ T ,  T ,  ?  , ? ,  T ]
         1 [ ? ,  T ,  ?  , T ,  ? ]
         2 [ ? ,  ? ,  T  , ? ,  ? ]
         3 [ ? ,  ? ,  ?  , T ,  T ]
         4 [ ? ,  ? ,  ?  , ? ,  T ] 
        """
        
        # Step.5 According to the precomputed table, do the backtracking.
        res = []
        def backtracking(start, curr):
            if start == n:
                res.append(curr[:])
                return
            for end in range(start, n):
                if pal_table[start][end]:
                    curr.append(s[start:end+1])
                    backtracking(end+1, curr)
                    curr.pop()
        # What happened here?
        """
        0 to 0 ~ 4 to 4 => ['a', 'a', 'b', 'a', 'a']
        0 to 0, 1 to 1, 2 to 2, 3 to 4 => ['a', 'a', 'b', 'aa']
        0 to 0, 1 to 3, 4 to 4 => ['a', 'aba', 'a']
        0 to 1, 2 to 2 ~ 4 to 4 => ['aa', 'b', 'a', 'a']
        0 to 1, 2 to 2, 3 to 4 = > ['aa', 'b', 'aa']
        0 to 4 => ['aabaa']
        """
        backtracking(0,[])
        return res
        
sol = ExplanationSolution()
print(sol.partition("aabaa"))