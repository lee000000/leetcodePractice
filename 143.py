'''
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from ListNode import *

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        last = None
        cur = slow
        while cur:
            temp = cur
            cur = cur.next
            temp.next = last
            last = temp


        # Merge
        h1, h2 = head, last
        while h2.next:
            temp1 = h1.next
            temp2 = h2.next
            h1.next = h2
            h1 = temp1
            h2.next = h1
            h2 = temp2
        return

def test():
    a = [1, 2, 3, 4, 5]
    head = List_to_Link(a).head
    sol = Solution()
    sol.reorderList(head)
    Link_to_List(head).print_list()


if __name__ == "__main__":
    test()
