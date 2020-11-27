/*
 * @lc app=leetcode.cn id=169 lang=javascript
 *
 * [169] 多数元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let res=0,cnt=0;
  for(let i=0;i<nums.length;i++){
      if(cnt==0) {
          res=nums[i];
          cnt++;
      }
      else{
          res==nums[i]?cnt++:cnt--;
      }
  }
  return res;
};
// @lc code=end

