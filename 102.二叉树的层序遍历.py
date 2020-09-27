#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        arr = [root]
        while len(arr):
            loop = arr[0:]
            arr = []
            temp = []
            for node in loop:
                temp.append(node.val)
                if node.left != None:
                    arr.append(node.left)
                if node.right != None:
                    arr.append(node.right)
            res.append(temp)
        return res
# @lc code=end
