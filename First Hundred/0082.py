# Definition for singly-linked list.
import copy
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
            if p2 == None or p1.val != p2.val:
                if t == None:
                    h = t = p1
                else:
                    t.next = p1
                    t = t.next
                t.next = None
                p1 = p2
                continue
            
            while p2 != None and p1.val == p2.val: p2 = p2.next
            p1 = p2
        
        return h