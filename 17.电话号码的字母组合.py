#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dict = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z'],
        ]
        if len(digits) == 1:
            return dict[int(digits[0], 10)]
        strs = []
        for s in digits:
            strs.append(dict[int(s, 10)])

        res = []
        temp = []
        for x in strs:
            temp = res[0:]
            res = []
            for item in x:
                if len(temp) > 0:
                    for s in temp:
                        res.append(s+item)
                else:
                    res.append(item)
        return res
# @lc code=end
