class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 从后向前循环，最后一个num+1 若num+1>9 则置为零，进入下一个循环，否则num+1 return 数组
        # length  = len(digits)
        for i in range(len(digits)-1,-1,-1):
            num = digits[i] + 1
            if num == 10:
                if i == 0:
                    digits[i] = 1
                    digits.append(0)
                else:
                    digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return digits

