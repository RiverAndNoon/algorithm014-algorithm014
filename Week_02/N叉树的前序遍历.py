# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : N叉树的前序遍历.py
# @time     : 2020/8/22 5:34 PM
# @desc     :

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            res.append(cur.val)
            stack.extend(cur.children[::-1])
        return res

        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     for child in root.children:
        #         helper(child)
        # helper(root)
        # return res