'''
328. Odd Even Linked List

Given a singly linked list, group all odd nodes

together followed by the even nodes. Please note

here we are talking about the node number and not the

value in the nodes.

You should try to do it in place. The program should

run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should

remain as it was in the input.

The first node is considered odd, the second node even and so on...

'''
from ListNode import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = head.next
        first_even = even

        while even and even.next:
            print(odd.val)

            print(odd.next.next.val)
            print(even.val)

            print(even.next.next.val)
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = first_even
        return head

def test():
    a = [1, 2, 3, 4, 5, 6]
    head = List_to_Link(a).head
    sol = Solution()
    retHead = sol.oddEvenList(head)
    Link_to_List(retHead).print_list()



if __name__ == "__main__":
    test()
