# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # prehead = ListNode()
        # prev = prehead

        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         prev.next = l1
        #         l1 = l1.next
        #     else:
        #         prev.next = l2
        #         l2 = l2.next
        #     prev = prev.next

        # if l1 == None:
        #     prev.next = l2
        # else:
        #     prev.next = l1

        # return prehead.next

        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2


