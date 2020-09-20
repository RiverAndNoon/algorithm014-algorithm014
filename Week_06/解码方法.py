# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 解码方法.py
# @time     : 2020/9/19 7:04 PM
# @desc     :

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        dp = [1, 0]
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1, n):
            dp.append(0)
            if s[i] != '0':
                dp[-1] += dp[-2]
            if s[i - 1:i + 1] >= '10' and s[i - 1:i + 1] <= '26':
                dp[-1] += dp[-3]
            dp.pop(0)

        return dp[-1]

