# 20260516
from typing import List
from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x_max, y_max = len(board), len(board[0])
        
        # Count words at first for bad test cases.
        board_count = Counter(ch for row in board for ch in row) # idk how this double for syntax work => ch from =>for row in board: for ch in row:
        """
        # 相當於在背後做了這件事：
        flat_list = []
        for row in board:           # 先拿出每一橫列 (row)
            for ch in row:          # 再拿出橫列裡的每一個字元 (ch)
                flat_list.append(ch)
        board_count = Counter(flat_list)
        """
        word_count = Counter(word)
        # 如果盤面上這個字母的總數量 (board_count[ch])，竟然比我單字裡需要的數量 (count) 還少，那根本不可能拼出來，直接回傳 False，連 DFS 都不用進去了。
        for ch, count in word_count.items(): # and also this
            if board_count[ch] < count:
                return False
        # idk how does these two lines work
        """
        假設 word 是 "AAAAAB"。
        word[0] 是 'A'，假設盤面上 'A' 有 100 個（board_count['A'] == 100）。
        word[-1] 是 'B'，假設盤面上 'B' 只有 1 個（board_count['B'] == 1）。

        如果我們從第一個字母 'A' 開始搜尋 DFS，因為盤面上有 100 個 'A'，程式會把這 100 個起點全部試過，產生幾萬條分支，走到最後才發現找不到 'B'。
        但這行程式碼發現 'B' 的數量 (1) < 'A' 的數量 (100)，所以它大筆一揮，把目標單字反轉成 "BAAAAA"。
        """
        if board_count[word[-1]] < board_count[word[0]]:
            word = word[::-1]
               
        def dfs(index, x, y):
            
            # Completely Make the word
            if index == len(word):
                return True
            # If exceed or the word on board != word[index]
            if x < 0 or x >= x_max or y < 0 or y >= y_max or board[x][y] != word[index]:
                return False
            # Make mark
            temp = board[x][y]
            board[x][y] = "#"
            # try 4 direction
            found = (dfs(index + 1, x + 1, y) or
                    dfs(index + 1, x - 1, y) or
                    dfs(index + 1, x, y + 1) or
                    dfs(index + 1, x, y - 1))
            # Erase the mark
            board[x][y] = temp
            
            return found
                
            
        for i in range(x_max):
            for j in range(y_max):
                if dfs(0, i, j):
                    return True
        
        return False


sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

# Array
# String
# Backtracking
# Depth-First Search
# Matrix

CoT:
1. Find the first digit, then use recursion to check if the neighbor word equals to next digit.
2. If not, return, If true, recursion starts again.

Answer CoT:
1. Pruning: Return False directly if there are not sufficient words in the matrix.
2. Reverse String: If the reversed word first char's count is less than original, then reverse it.
3. DFS:
    - if word is complete the index == len(word) => word complete
    - If exceed or the word on board != word[index]
    - Mark the current word as # 
    - using or and recursion return for checking
    - After checking remove the mark

Time Complexity: O(N^3 * L) N represent for number of cells in the board and L is the length of the word to be matched.
"""

"""
If in Java
  # 字元轉 ASCII 碼
  // 1. 統計盤面上所有字元的數量 (取代 board_count)
  // ASCII 字元最多 128 個，陣列預設值為 0
  int[] boardCount = new int[128]; 
  for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[0].length; j++) {
          // board[i][j] 是一個字元，例如 'A'，它會自動轉為 ASCII 碼 65 作為 index
          boardCount[board[i][j]]++; 
      }
  }

  // 2. 統計目標單字的字元數量，並提早審判 (取代 word_count 與 for 迴圈)
  int[] wordCount = new int[128];
  for (char ch : word.toCharArray()) {
      wordCount[ch]++;
      // 如果單字需要的某個字母數量，已經大於盤面上的總數，直接宣告失敗
      if (wordCount[ch] > boardCount[ch]) {
          return false;
      }
  }

  // 3. 聰明的起點：比較頭尾字母的頻率，決定是否反轉字串
  char firstChar = word.charAt(0);
  char lastChar = word.charAt(word.length() - 1);

  if (boardCount[lastChar] < boardCount[firstChar]) {
      // Java 反轉字串的標準寫法
      word = new StringBuilder(word).reverse().toString(); 
  }
"""