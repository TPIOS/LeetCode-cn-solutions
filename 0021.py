# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        tmp = ListNode(0)
        res.next = tmp

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cc = ListNode(l1.val)
                tmp.next = cc
                tmp = cc
                l1 = l1.next
            else:
                cc = ListNode(l2.val)
                tmp.next = cc
                tmp = cc
                l2 = l2.next
        
        if l2 != None:
            while l2 != None:
                cc = ListNode(l2.val)
                tmp.next = cc
                tmp = cc
                l2 = l2.next
        elif l1 != None:
            while l1 != None:
                cc = ListNode(l1.val)
                tmp.next = cc
                tmp = cc
                l1 = l1.next
        
        return res.next.next

                