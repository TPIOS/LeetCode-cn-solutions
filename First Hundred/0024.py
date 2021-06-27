# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        new_head = head.next
        new_tail = head

        head = head.next.next
        new_head.next = new_tail
        new_tail.next = None

        while head != None and head.next != None:
            p1 = head
            p2 = head.next
            head = head.next.next
            new_tail.next = p2
            p2.next = p1
            new_tail = p1
            new_tail.next = None
        
        if head != None:
            new_tail.next = head
            new_tail = head
            new_tail.next = None
        
        return new_head