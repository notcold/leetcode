#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        map = {5: 0, 10: 0, 20: 0}
        if bills[0] > 5:
            return False
        # 遍历数组
        for p in bills:
            if (p == 5):
                map[5] += 1
            if (p == 10):
                map[10] += 1
                map[5] -= 1
            if (p == 20):
                if map[10] > 0:
                    map[10] -= 1
                    map[5] -= 1
                else:
                    map[5] -= 3
            if map[5] < 0 or map[10] < 0:
                return False
        if map[5] < 0 or map[10] < 0:
            return False
        else:
            return True
# @lc code=end
