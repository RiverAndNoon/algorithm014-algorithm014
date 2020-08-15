class Solution:
    def twoSum(self, nums, target):
        # l = []
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             l.extend([i, j])
        #             return l
        if len(nums) < 2:
            return
        tmp = nums
        nums = sorted(nums)
        # print(nums)
        left = 0
        right = len(nums) - 1
        while right > left:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                break
        if right == left:
            return
        n = tmp.index(nums[left])
        tmp.pop(n)
        m = tmp.index(nums[right])
        if m >= n:
            m += 1

        return [n, m]