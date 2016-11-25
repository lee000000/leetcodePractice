'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values
in the list, only nodes itself can be changed.
'''
from ListNode import *
from pprint import pprint
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next,
        # we need to change those three references. Instead of thinking about
        # in what order I change them, I just change all three at once.
        pre = self
        pre.next = head

        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


def test():
    a = [1, 2, 3, 4, 5, 6]
    head = List_to_Link(a).head
    sl = Solution()
    b = sl.swapPairs(head)

    Link_to_List(b).print_list()


if __name__ == "__main__":
    test()
