class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # i, j = 0, 0
        # while j < n:
        #     if i >= m+j: 
        #         nums1[i:i+n-j] = nums2[j:n]
        #         break
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     else:
        #         nums1[i], nums1[i+1:] = nums2[j], nums1[i:len(nums1)-1]
        #         j += 1; i += 1
        # return nums1

        # 定义两个指针分别指向nums1、nums2的末尾
        # 定义两个指针分别指向nums1、nums2的末尾
        num1_c = m - 1
        num2_c = n - 1
        k = m + n - 1
        while num2_c >= 0 or num1_c >= 0:
            if num1_c < 0:
                nums1[k] = nums2[num2_c]
                num2_c -= 1

            elif num2_c < 0:
                nums1[k] = nums1[num1_c]
                num1_c -= 1
            elif nums1[num1_c] <= nums2[num2_c]:
                nums1[k] = nums2[num2_c]
                num2_c -= 1
            else:
                nums1[k] = nums1[num1_c]
                num1_c -= 1
            k -= 1
        return nums1

