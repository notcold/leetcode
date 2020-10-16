#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []

        def dfs(node):
            if node:
                arr.append(node.val)
                for no in node.children:
                    dfs(no)
        dfs(root)
        return arr
        
        # @lc code=end

