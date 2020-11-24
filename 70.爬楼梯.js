/*
 * @lc app=leetcode.cn id=70 lang=javascript
 *
 * [70] 爬楼梯
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n == 1) return 1;
  if (n == 2) return 2;
  const arr = [0, 1, 2];
  for (let index = 3; index < n + 1; index++) {
    arr[index] = arr[index - 1] + arr[index - 2];
  }
  return arr[n]
};
// @lc code=end
