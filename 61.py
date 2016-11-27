'''
61. Rotate List

Given a list, rotate the list to the right by k places,

where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

from ListNode import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = self
        pre.next = head
        dummy = ListNode(0)
        count = 1
        while head.next:
            count += 1
            head = head.next
        if count == k:
            return self.next
        head.next = self.next
        head = self.next
        step = 1
        print(count)
        while step < count - (k % count):
            head = head.next
            step += 1

        pre.next = head.next
        head.next = None
        return pre.next


def test():
    a = [1, 2, 3]
    head = List_to_Link(a).head
    sol = Solution()
    rhead = sol.rotateRight(head, 4)
    Link_to_List(rhead).print_list()


if __name__ == "__main__":
    test()
