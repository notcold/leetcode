#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n-2
        if n == 1:
            return True
        while i != -1:
            if nums[i] > 0:
                i -= 1
                continue
            for k in range(i-1, -1, -1):
                if k+nums[k] > i:
                    i = k
                    break
            else:
                return False
        return True
# @lc code=end
