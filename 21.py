'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it a
s a new list. The new list should be made by splicing together
the nodes of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if None in (l1, l2):
            return l1 or l2
        cur = ListNode(0)
        head = cur

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next # <<<< does not change head.next?


        if not l1:
            cur.next = l2

        if not l2:
            cur.next = l1

        return head.next


def test():
    # a = [1, 1, 2, 4, 5]
    # b = [1, 3, 6]
    #
    # sl = Solution()
    # headA = List_to_Link(a).head
    # headB = List_to_Link(b).head
    #
    # Link_to_List(sl.mergeTwoLists(headA, headB)).print_list()


    node = ListNode(1)
    dummy = cur = ListNode(0)
    cur.next = node
    cur = cur.next
    print("cur,", cur.val)
    print("dummy, ", dummy.val)
    print("dummy next, ", dummy.next.val)


if __name__ == "__main__":
    test()
