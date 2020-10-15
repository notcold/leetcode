#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def dfs(node, s):
            if not node:
              return False
            """
            docstring
            """
            if not node.left and not node.right:
                if node.val + s == sum:
                    return True
                else:
                    return False
            return dfs(node.left, s+node.val) or dfs(node.right, s+node.val)

        return dfs(root, 0)
# @lc code=end
