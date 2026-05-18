# 20260518
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid//col][mid%col] == target:
                return True
            elif matrix[mid//col][mid%col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(sol.searchMatrix([[1], [3], [5], [7], [9], [11], [13], [15], [17], [19],    [21], [23], [25], [27], [29], [31], [33], [35], [37], [39],    [41], [43], [45], [47], [49], [51], [53], [55], [57], [59],    [61], [63], [65], [67], [69], [71], [73], [75], [77], [79],    [81], [83], [85], [87], [89], [91], [93], [95], [97], [99]], 3))
print(sol.searchMatrix([[1],[3],[5],[6]], 3))
print(sol.searchMatrix([[1, 3]], 3))
print(sol.searchMatrix([[1, 3]], 2))
print(sol.searchMatrix([[1]], 1))

"""
just a simple tip always remember
in 2d matrix of m*n
no. of rows = mid/n
no. of cols= mid%n

# You must write a solution in O(log(m * n)) time complexity.
"""