#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        arr = set([])
        nums.sort()
        print(nums)
        for i in range(length-2):
            left = i+1
            right = length-1
            if nums[i] > 0:
                break
            if i>0 and nums[i-1] == nums[i]:
                continue
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    arr.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    left += 1
       
        return list(arr)
# @lc code=end
