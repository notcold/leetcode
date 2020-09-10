#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        t = 0
        s = 0
        result = 0
        while right < len(A):
            if t == K and A[right] == 0:
                result = max(result, right - left)
                if A[left] == 0:
                    t -= 1
                    left += 1
                    # right += 1
                else:
                    left += 1
            else:
                if A[right] == 0:
                    t += 1
                    right += 1
                else:
                    right += 1

        result = max(result, right - left)
        return result


# @lc code=end

