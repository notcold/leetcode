#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序有利于后面剪枝
        candidates.sort()
        n = len(candidates)
        # 回溯

        def backtrack(index, sum, temp):
            if sum > target:
                return
            if sum == target:
                res.append(temp)
            for j in range(index, n):
                # 超出的直接跳过
                if candidates[j] + sum > target:
                    break
                backtrack(j, sum+candidates[j], temp+[candidates[j]])
        # 入口开始
        backtrack(0, 0, [])
        return res
# @lc code=end
