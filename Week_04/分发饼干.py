# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 分发饼干.py
# @time     : 2020/9/2 5:38 PM
# @desc     :

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # g.sort(reverse = True)
        # s.sort(reverse = True)
        # count = 0
        # max_length = max(len(g), len(s))
        # for i in range(max_length):
        #     if len(g)>0 and len(s)>0 and s[-1] >= g[-1]:
        #         g.pop()
        #         s.pop()
        #         count += 1
        #     elif len(g)>0 and len(s)>0:
        #         s.pop()
        # return count
        g.sort()
        s.sort()
        gi = si = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi

