#
# @lc app=leetcode.cn id=1293 lang=python3
#
# [1293] 网格中的最短路径
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        if k > m+n-3:
            return m+n-2
        visited = set([(0, 0, k)])
        step = 0
        queue = collections.deque([(0, 0, k)])
        while len(queue):
            step += 1
            le = len(queue)
            for _ in range(le):
                q = queue.popleft()
                x, y, rest = q
                for (dx, dy) in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy, rest) not in visited:
                        if m-1 == dx and n-1 == dy:
                            return step
                        if grid[dx][dy] != 1:
                            queue.append((dx, dy, rest))
                            visited.add((dx, dy, rest))
                        elif grid[dx][dy] == 1 and rest > 0 and (dx, dy, rest-1) not in visited:
                            queue.append((dx, dy, rest-1))
                            visited.add((dx, dy, rest-1))
        return -1


# @lc code=end
