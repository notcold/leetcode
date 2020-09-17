#
# @lc app=leetcode.cn id=1293 lang=python3
#
# [1293] 网格中的最短路径
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        myList = [[0] * len(grid[0])] * len(grid)
        myList[0][0] = 1

        def loop(m: int, n: int, k: int) -> int:
            print(m,n,k)
            if myList[m][n] != 0:
                return myList[m][n]
            l, r, t, b = m * n, m * n, m * n, m * n
            if m - 1 >= 0:
                if grid[m - 1][n] == 1 and k == 0:
                    t = m * n
                else:
                    k = k - 1 if grid[m - 1][n] == 1 else k
                    t = loop(m - 1, n, k - 1)
            if n - 1 >= 0:
                if grid[m][n - 1] == 1 and k == 0:
                    l = m * n
                else:
                    k = k - 1 if grid[m][n - 1] == 1 else k
                    l = loop(m, n - 1, k)

            if m + 1 < len(grid) - 1:
                if grid[m + 1][n] == 1 and k == 0:
                    b = m * n
                else:
                    k = k - 1 if grid[m + 1][n] == 1 else k
                    b = loop(m + 1, n, k - 1)

            if n + 1 < len(grid[m]) - 1:
                if grid[m][n + 1] == 1 and k == 0:
                    r = m * n
                else:
                    k = k - 1 if grid[m][n + 1] == 1 else k
                    r = loop(m, n + 1, k)

            myList[m][n] = min(l, r, t, b) + 1
            return myList[m][n]

        return loop(len(grid) - 1, len(grid[0]) - 1, k)


# @lc code=end

