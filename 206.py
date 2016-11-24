'''
206. Reverse Linked List

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next:
            return True

        slow = head
        fast = head

        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        if not fast:
            print(slow.val)
            print(fast.val)
            slow = slow.next

        left = head
        right = self.reverse(slow)


        while (right.next):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


    def reverse(self, head):
        if not head or not head.next:
            return head

        pre = None
        current = head

        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        return pre
