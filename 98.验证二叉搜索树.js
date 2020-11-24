/*
 * @lc app=leetcode.cn id=98 lang=javascript
 *
 * [98] 验证二叉搜索树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  if (root == null) {
    return true;
  }
  const stack = []
  let inorder = -Infinity;

  while (stack.length || root !== null) {
    while (root !== null) {
      // 左子节点入栈
      stack.push(root);
      root = root.left;
    }
    //
    root = stack.pop();

    if (root.val <= inorder) {
      return false;
    }
    inorder = root.val;
    root = root.right;
  }
  return true;
};
// @lc code=end
