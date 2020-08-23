# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 二叉树的前序遍历.py
# @time     : 2020/8/22 5:35 PM
# @desc     :

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

        # res = []
        # stack = []
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         res.append(root.val)
        #         root = root.left
        #     else:
        #         root = stack.pop()
        #         root = root.right
        # return res

        # res = []
        # def dfs(root):
        #     if root:
        #         res.append(root.val)
        #         dfs(root.left)
        #         dfs(root.right)
        # dfs(root)
        # return res