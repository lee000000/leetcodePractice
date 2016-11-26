'''
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list
and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list
   becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

from ListNode import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # this is a comment for git stage test
        fast = slow = self
        self.next = head
        while fast.next:
            if n <= 0:
                slow = slow.next
            fast = fast.next
            n -= 1
        if slow.next:
            slow.next = slow.next.next
        return self.next

def test():
    a = [1, 2]
    head = List_to_Link(a).head
    sol = Solution()
    ret = sol.removeNthFromEnd(head, 2)
    Link_to_List(ret).print_list()


if __name__ == "__main__":
    test()
