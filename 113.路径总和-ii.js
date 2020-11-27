/*
 * @lc app=leetcode.cn id=113 lang=javascript
 *
 * [113] 路径总和 II
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

function backtrack(root, sum, res, tempList) {
  if (root === null) return;
  if (root.left === null && root.right === null && sum === root.val)
    return res.push([...tempList, root.val]);

  tempList.push(root.val);
  backtrack(root.left, sum - root.val, res, tempList);

  backtrack(root.right, sum - root.val, res, tempList);
  tempList.pop();
}

var pathSum = function (root, sum) {
  if (root === null) return [];
  const res = [];
  backtrack(root, sum, res, []);
  return res;
};
// @lc code=end

