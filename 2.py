'''
2. Add Two Numbers

You are given two linked lists representing two non-negative

numbers. The digits are stored in reverse order and each of

their nodes contain a single digit. Add the two numbers and

return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

from ListNode import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

    def addTwoNumbers_extra_zero(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2

        cur = ListNode(0)

        carry = 0
        pre = None
        while l1 or l2 or carry:
            if l1:
                carry = carry + l1.val
                l1 = l1.next
            if l2:
                carry = carry + l2.val
                l2 = l2.next
            temp = ListNode(carry % 10)
            cur.next = temp
            temp.next = pre
            pre, temp = temp, cur
            carry = carry // 10

        return cur






def test():
    l1 = [1, 2, 3]
    l2 = [0, 9, 1]
    headA = List_to_Link(l1).head
    headB = List_to_Link(l2).head

    sol = Solution()
    headC = sol.addTwoNumbers(headA, headB)
    Link_to_List(headC).print_list()


if __name__ == "__main__":
    test()
