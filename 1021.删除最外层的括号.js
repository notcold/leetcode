/*
 * @lc app=leetcode.cn id=1021 lang=javascript
 *
 * [1021] 删除最外层的括号
 */

// @lc code=start
/**
 * @param {string} S
 * @return {string}
 */
var removeOuterParentheses = function (S) {
  let stack = [];
  let res = "";
  for (let i = 0; i < S.length; i++) {
    let item = S[i];
    if (item === ")") {
      stack.pop();
    }
    if (stack.length != 0) {
      res += item;
    }
    if (item === "(") {
      stack.push(item);
    }
  }
  return res;
};
// @lc code=end
