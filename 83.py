'''
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

from ListNode import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head






def test():
    a = [1, 1, 2, 2, 3, 4, 4, 5, 6]
    la = List_to_Link(a)
    current = la.head
    sl = Solution()
    lst = Link_to_List(sl.deleteDuplicates(current))
    lst.print_list()




if __name__ == "__main__":
    test()
