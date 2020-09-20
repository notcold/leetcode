#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        large = max(weights)
        length = len(weights)
        s = sum(weights)
        if length == D:
            return large
        cap = 0
        while cap < s:
            mid = cap + (s - cap)//2
            print(mid)
            cur = mid
            day = D
            for weight in weights:
                if weight > mid:
                    day = -1
                    break
                if cur < weight:
                    cur = mid
                    day -= 1
                cur -= weight
            if day > 0:
                s = mid
            else:
                cap = mid + 1
        return cap
# @lc code=end
