# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 两数之和.py
# @time     : 2020/8/22 5:33 PM
# @desc     :

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) <= 1:
            return False
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target - nums[i]] = i

        # if len(nums) < 2:
        #     return
        # temp = nums
        # temp = sorted(temp)
        # left = 0
        # right = len(temp) - 1
        # while left < right:
        #     if temp[left] + temp[right] > target:
        #         right -= 1
        #     elif temp[left] + temp[right] < target:
        #         left += 1
        #     else:
        #         break
        # n = nums.index(temp[left])
        # nums.pop(n)
        # m = nums.index(temp[right])
        # if m >= n:
        #     m += 1
        # return [n,m]