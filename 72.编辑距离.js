/*
 * @lc app=leetcode.cn id=72 lang=javascript
 *
 * [72] 编辑距离
 */

// @lc code=start
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
  const len1 = word1.length;
  const len2 = word2.length;
  const arr = new Array(len2);
  const dp = new Array(len1);
  dp.fill(arr);
  /** 
   * [
   *  [0,1,   2,    3]
   *  [1,null,null,null]
   *  [2,null,null,null]
   *  [3,null,null,null]
   *  [4,null,null,null]
   *  [5,null,null,null]
   * ]
   */
  for (let i = 0; i <= len1; i++) {
    dp[i] = [...arr];
    dp[i][0] = i;
  }
  for (let j = 0; j <= len2; j++) {
    dp[0][j] = j;
  }
  for (let i = 1; i <= len1; i++) {
    for (let j = 1; j <= len2; j++) {
      if (word1[i - 1] == word2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] =
          1 + Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
      }
    }
  }
  return dp[len1][len2]
};
// @lc code=end
