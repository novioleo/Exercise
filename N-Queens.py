# https://leetcode.com/problems/n-queens/description/
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        to_return = []

        def dfs(to_display, cur_rows, diag_1, diag_2, row_index, rows):
            if row_index == 0:
                to_return.append(to_display)
            else:
                for i in range(rows):
                    to_place = 1 << i
                    if cur_rows | to_place != cur_rows and \
                                            diag_1 | (1 << (i + rows - row_index)) != diag_1 and \
                                            diag_2 | (1 << (i + row_index)) != diag_2:
                        t_to_display = to_display.copy()
                        to_append = ['.' for _ in range(rows)]
                        to_append[i] = 'Q'
                        t_to_display.append(''.join(to_append))
                        dfs(t_to_display, cur_rows | to_place, diag_1 | (1 << (i + rows - row_index)),
                            diag_2 | (1 << (i + row_index)), row_index - 1, rows)

        dfs([], 0, 0, 0, n, n)
        return to_return

if __name__ == '__main__':
    s = Solution()
    import time
    cur = time.time()
    print(s.solveNQueens(16))
    print(time.time()-cur)