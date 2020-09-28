#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = []

        def takeSecond(elem):
            return elem[1]

        intervals.sort(key=takeSecond)

        for item in intervals:
            if len(arr) == 0 or item[0] > arr[-1][1]:
                arr.append(item)
            else:
                temp = item
                while len(arr) and temp[0] <= arr[-1][1]:
                        temp[0] = min(temp[0], arr[-1][0])
                        temp[1] = max(temp[1], arr[-1][1])
                        arr.pop()
                arr.append(temp)
        return arr
# @lc code=end
