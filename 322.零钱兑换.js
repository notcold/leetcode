/*
 * @lc app=leetcode.cn id=322 lang=javascript
 *
 * [322] 零钱兑换
 */

// @lc code=start
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  if (amount == 0) {
    return 0;
  }
  const dp = new Array(amount + 1);
  dp.fill(Number.MAX_SAFE_INTEGER);
  for (let index = 0; index < coins.length; index++) {
    let coin = coins[index];
    dp[coin] = 1;
  }
  for (let index = 1; index < amount + 1; index++) {
    if (dp[index] != Number.MAX_SAFE_INTEGER) {
      continue;
    }
    let d = Math.min(
      ...coins.map((coin) =>
        index - coin >= 0 ? dp[index - coin] : Number.MAX_SAFE_INTEGER
      )
    );
    dp[index] = d !== Number.MAX_SAFE_INTEGER ? d + 1 : Number.MAX_SAFE_INTEGER;
  }
  return dp[amount] != Number.MAX_SAFE_INTEGER ? dp[amount] : -1;
};
// @lc code=end
