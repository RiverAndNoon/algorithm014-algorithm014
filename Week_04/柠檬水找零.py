# -*- coding:utf-8 -*-

# @auther   : shaomeng
# @project  : algorithm014-algorithm014
# @file     : 柠檬水找零.py
# @time     : 2020/9/2 5:37 PM
# @desc     :

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True