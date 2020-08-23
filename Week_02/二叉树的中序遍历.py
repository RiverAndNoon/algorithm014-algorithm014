# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 二叉树的中序遍历.py
# @time     : 2020/8/22 5:34 PM
# @desc     :

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

        # result = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     result.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return result

        # res = []
        # stack = []
        # while stack or root:
        #     # 不断向左子树走，没走一步就将当前节点保存到栈中
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:#当前节点为空则说明走到头了，从栈中弹出节点并保存。
        #         tmp = stack.pop()
        #         res.append(tmp.val)
        #         # 转向当前节点的右子树，重复上面过程。
        #         root = tmp.right
        # return res