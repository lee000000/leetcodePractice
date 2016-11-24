# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class List_to_Link(object):
    def __init__(self, sequence):
        if not sequence:
            self.head = None
        self.head = ListNode(sequence[0])
        current = self.head
        for item in sequence[1:]:
            current.next = ListNode(item)
            current = current.next


class Link_to_List(object):
    def __init__(self, head):
        if not head:
            self.lst = None
        self.lst = []
        while head:
            self.lst.append(head)
            head = head.next


    def print_list(self):
        a = []
        for item in self.lst:
            a.append(item.val)
        print(a)
