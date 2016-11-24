'''
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import gc
from ListNode import *


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        ptr_a = headA
        ptr_b = headB

        len_a = 0
        len_b = 0

        while ptr_a:
            len_a += 1
            ptr_a = ptr_a.next

        while ptr_b:
            len_b += 1
            ptr_b = ptr_b.next

        ptr_a = headA
        ptr_b = headB

        step = abs(len_a - len_b)
        if (len_a > len_b):
            while step:
                ptr_a = ptr_a.next
                step -= 1
        else:
            while step:
                ptr_b = ptr_b.next
                step -= 1

        while ptr_a != ptr_b:
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
            if ptr_a == ptr_b:
                print(ptr_a.val)
                return ptr_a
        print("None")
        return None

    def getIntersectionNode_fast(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        ptr_a = headA
        ptr_b = headB

        while ptr_a != ptr_b:
            if ptr_a:
                ptr_a = ptr_a.next
            else:
                ptr_a = headB

            if ptr_b:
                ptr_b = ptr_b.next
            else:
                ptr_b = headA
        print(ptr_a.val)
        return ptr_a


def test():
    nd1 = ListNode(1)
    nd2 = ListNode(2)
    nd3 = ListNode(3)
    nd4 = ListNode(4)
    nd5 = ListNode(5)
    nd6 = ListNode(6)
    nd7 = ListNode(7)
    nd8 = ListNode(8)
    nd9 = ListNode(9)
    nd1.next = nd2
    nd2.next = nd3
    nd3.next = nd4
    nd4.next = nd5
    nd5.next = nd6
    nd7.next = nd8
    nd8.next = nd9
    nd9.next = nd2

    headA = nd1
    headB = nd9


    sl = Solution()
    assert sl.getIntersectionNode_fast(headA, headB) == nd2



if __name__ == "__main__":
    test()
