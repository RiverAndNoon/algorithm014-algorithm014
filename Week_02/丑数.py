# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 丑数.py
# @time     : 2020/8/22 5:35 PM
# @desc     :

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # 递归
        if num == 0:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            return self.isUgly((num // 2))
        if num % 3 == 0:
            return self.isUgly((num // 3))
        if num % 5 == 0:
            return self.isUgly((num // 5))
        return False

        # 迭代
        # for p in [2, 3, 5]:
        #     while num % p == 0 and num > 0:
        #         num //= p
        # return num == 1