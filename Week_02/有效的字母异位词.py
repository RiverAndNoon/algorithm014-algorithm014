# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 有效的字母异位词.py
# @time     : 2020/8/22 5:33 PM
# @desc     :

import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return collections.Counter(s) == collections.Counter(t)

        # return abs(sum([ord(x)**0.5 for x in s])-sum([ord(y)**0.5 for y in t]))<1e-5

        if len(s) != len(t):
            return False

        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                return False
        for value in dic.values():
            if value != 0:
                return False
        return True