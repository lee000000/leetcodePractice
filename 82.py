'''
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that

have duplicate numbers, leaving only distinct numbers

from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        pre = self
        pre.next = head
        while head and head.next:
            if (head.val == head.next.val):
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                pre.next = head
                pre = pre.next

            head = head.next
        pre.next = head
        return self.next


def test():
    a = [1, 2, 4, 4, 3, 3, 5, 6]
    head = List_to_Link(a).head
    sol = Solution()
    rhead = sol.deleteDuplicates(head)
    Link_to_List(rhead).print_list()


if __name__ == "__main__":
    test()
