#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def dfs(tree, copy):
            if tree == None or copy == None:
                if tree == copy:
                    return True
                else:
                    return False
            if tree != None and copy != None and tree.val == copy.val:
                return dfs(tree.left, copy.left) and dfs(tree.right, copy.right)
            else:
                return False
        return dfs(p, q)
# @lc code=end
