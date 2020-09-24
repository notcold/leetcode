#
# @lc app=leetcode.cn id=848 lang=python3
#
# [848] 字母移位
#

# @lc code=start
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        arr = []
        length = len(shifts)
        str = ""
        for i in range(length):
            shifts[i] = shifts[i] % 26
        for x in range(length):
            k = ord(S[x])+sum(shifts[x:]) % 26
            cha = k if k < 123 else k - 26
            str += chr(cha)
        return str
# @lc code=end
