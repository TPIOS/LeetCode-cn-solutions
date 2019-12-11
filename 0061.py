import copy
class Solution:
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        n = 0
        p1 = head
        while p1 != None:
            p1 = p1.next
            n += 1
        
        if k % n == 0: return head
        
        k %= n
        p1 = head

        for i in range(n-k-1): p1 = p1.next
        h = p1.next
        p1.next = None
        t = h
        while t.next != None: t = t.next
        t.next = head

        return h