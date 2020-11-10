/*
 * @lc app=leetcode.cn id=110 lang=javascript
 *
 * [110] 平衡二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function (root) {
  if (!root) {
    return !!1;
  }
  if (Math.abs(dfs(root.left, 0) - dfs(root.right, 0)) > 1) {
    return false;
  }
  return isBalanced(root.left) && isBalanced(root.right);
};
const dfs = (node, depth) => {
  if (!node) {
    return 0;
  }
  const l = dfs(node.left, depth + 1);
  const r = dfs(node.right, depth + 1);
  return Math.max(l, r) + 1;
};
// @lc code=end
