#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.ismirror(root.left, root.right)

    def ismirror(self,node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False
        return self.ismirror(node1.left, node2.right) and self.ismirror(node1.right, node2.left)
# @lc code=end
