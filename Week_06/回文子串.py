# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 回文子串.py
# @time     : 2020/9/19 6:44 PM
# @desc     :

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n)]

        for i in range(n):
            dp[i][i], dp[i][i+1] = 1, 1
        count = n
        for i in range(n-1, -1, -1):
            for j in range(i+2, n+1):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j-1]
                if dp[i][j]:
                    count += 1
        return count