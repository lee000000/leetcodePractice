'''
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

from ListNode import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        walk = head
        print(walk.val)
        chase = head

        while (chase.next) and (chase.next.next):
            print("walk,", walk.val)
            print("chase,", chase.val)

            walk = walk.next
            chase = chase.next.next

            if walk == chase:
                print("True")
                return True

        print("False")
        return False

# def test():
#     nd1 = ListNode(1)
#     nd2 = ListNode(2)
#     nd3 = ListNode(3)
#     nd4 = ListNode(4)
#     nd5 = ListNode(5)
#     nd6 = ListNode(6)
#     nd7 = ListNode(7)
#     nd8 = ListNode(8)
#     nd9 = ListNode(9)
#     nd1.next = nd2
#     nd2.next = nd3
#     nd3.next = nd4
#     nd4.next = nd5
#     nd5.next = nd6
#     nd6.next = nd7
#     nd7.next = nd8
#     nd8.next = nd9
#     nd9.next = nd2
#
#     headA = nd1
#
#
#     sl = Solution()
#     assert sl.hasCycle(headA) == True


if __name__ == "__main__":
    test()
