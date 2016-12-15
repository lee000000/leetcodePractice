'''
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order,

convert it to a height balanced BST.
[1, 2, 3, 4, 5, 6, 7]
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.sortedListToBSTH(head, None)


    def sortedListToBSTH(self, start, end):
        if not start or start == end:
            return None
        slow = fast = start
        while fast.next != end and fast.next.next != end:
            slow = slow.next
            fast = fast.next.next
        if not fast:
            print("None")

        root = TreeNode(slow.val)
        root.left = self.sortedListToBSTH(start, slow)
        root.right = self.sortedListToBSTH(slow.next, end)
        return root
