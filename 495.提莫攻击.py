#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        if len(timeSeries) == 1:
            return duration
        time = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] >= duration:
                time += duration
            else:
                time += timeSeries[i] - timeSeries[i - 1]

        return time + duration


# @lc code=end

