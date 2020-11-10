/*
 * @lc app=leetcode.cn id=746 lang=javascript
 *
 * [746] 使用最小花费爬楼梯
 */

// @lc code=start
/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
  const len = cost.length
    for (let index = 2; index < cost.length; index++){
      cost[index] = cost[index] + Math.min(cost[index-1],cost[index-2])
    }
  return Math.min(cost[len-1],cost[len-2])
};
// @lc code=end

