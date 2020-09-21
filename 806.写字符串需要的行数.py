#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        row = 1
        w = 0
        left = 100
        for str in S:
            cur = widths[ord(str)-97]
            if left < cur:
                left = 100 - cur
                row += 1
                w = cur
            else:
                left -= cur
                w += cur
        return [row, w]
# @lc code=end
