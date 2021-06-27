# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head == None: return head
        p1 = head
        h = t = None
        while p1 != None:
            p2 = p1.next
            if t == None:
                h = t = ListNode(p1.val)
            else:
                t.next = ListNode(p1.val)
                t = t.next
            while p2 != None and p2.val == p1.val: p2 = p2.next
            p1 = p2
        return h
