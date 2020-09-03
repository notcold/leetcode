#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def loop(str, lt, r, limit):
            if lt == limit and r == limit:
                result.append(str)
                return
            if lt == r:
                loop(str+'(', lt+1, r, limit)
            else:
                if lt < limit:
                    loop(str+'(', lt+1, r, limit)
                if r < limit:
                    loop(str+')', lt, r+1, limit)

        loop("", 0, 0, n)
        return result
# @lc code=end
