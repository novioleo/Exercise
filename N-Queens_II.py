# https://leetcode.com/problems/n-queens-ii/description/
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        global count
        count = 0

        def dfs(cur_rows, diag_1, diag_2, row_index, rows):
            if row_index == 0:
                globals()['count'] += 1
            else:
                for i in range(rows):
                    to_place = 1 << i
                    t_cur_rows = cur_rows | to_place
                    t_diag_1 = diag_1 | (1 << (i + rows - row_index))
                    t_diag_2 = diag_2 | (1 << (i + row_index))
                    if t_cur_rows != cur_rows and t_diag_1 != diag_1 and t_diag_2 != diag_2:
                        dfs(t_cur_rows, t_diag_1, t_diag_2, row_index - 1, rows)

        dfs(0, 0, 0, n, n)
        return count


if __name__ == '__main__':
    s = Solution()
    for rows in range(4,14):
        count = 0
        # rows = 16
        s.totalNQueens(rows)
        print(rows, ':', count)
