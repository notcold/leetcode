#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ddd = {}
        lenght = len(nums)
        for item in nums:
            if item in ddd:
                ddd[item] = ddd[item] + 1
            else:
                ddd[item] = 1

        lt = []
        for key, value in ddd.items():
            if value > lenght/3:
                lt.append(key)
        return lt

# @lc code=end
