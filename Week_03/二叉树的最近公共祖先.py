# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 二叉树的最近公共祖先.py
# @time     : 2020/8/26 4:32 PM
# @desc     :

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root

        def helper(root, p, q):
            if not root or root == p or root == q:
                return root

            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            if left and right:
                return root
            if left:
                return left
            if right:
                return right

        res = helper(root, p, q)
        return res