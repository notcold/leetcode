#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        l = m + n-2
        c = min(m, n)-1
        print(l, c)

        def part(num,min):
            if num == min:
                return 1
            return num * part(num-1,min)

        return int(part(l,l-c)/part(c,1))
# @lc code=end
