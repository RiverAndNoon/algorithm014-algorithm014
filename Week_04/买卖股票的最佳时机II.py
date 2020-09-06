# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 买卖股票的最佳时机II.py
# @time     : 2020/9/2 5:38 PM
# @desc     :

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        earn = 0
        for i in range(len(prices)-1):
            tmp = prices[i+1] - prices[i]
            if tmp > 0:
                earn += tmp
        return earn