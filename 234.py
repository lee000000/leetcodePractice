'''
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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

        ptr = self.reverseList(head)

        count = 0
        while head.next:
            count += 1

        while count > (0.5 * count):
            if ptr.val != head.val:
                return False
            ptr = ptr.next
            head = head.next
        return True

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if None == head:
            return
        if None == head.next:
            return head

        current = head
        pre = None

        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        return pre
