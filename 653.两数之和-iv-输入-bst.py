#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        a=set()
        find=0
        def dfs(r):
            nonlocal find
            if r:
                dfs(r.left)
                if k-r.val in a:find=1
                a.add(r.val)
                dfs(r.right)
        dfs(root)
        return True if find else False
# @lc code=end

