# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 最长有效括号.py
# @time     : 2020/9/19 6:55 PM
# @desc     :

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res
