# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 前K个高频元素.py
# @time     : 2020/8/22 5:36 PM
# @desc     :

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        import collections
        dic = collections.Counter(nums)
        # return heapq.nlargest(k, dic.keys(), key=dic.get)

        queue = []
        res = []
        for i in dic:
            heapq.heappush(queue, (-dic[i], i))
        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])
        return res


