#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序有利于后面剪枝
        candidates.sort()
        n = len(candidates)
        # 回溯

        def backtrack(index, sum, temp):
            if sum > target:
                return
            if sum == target:
                res.append(temp[:])
            for j in range(index, n):
                # 超出的直接跳过
                if candidates[j] > target:
                    break
                if j > index and candidates[j] == candidates[j-1]:
                    continue
                backtrack(j+1, sum+candidates[j], temp+[candidates[j]])
        # 入口开始
        backtrack(0, 0, [])
        return res

# @lc code=end
