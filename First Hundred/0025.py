class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.h = None
        self.t = None
    
    def reverseList(self):
        if self.h == None: return
        h = t = None
        p = self.h
        while p != None:
            self.h = self.h.next
            if h == None:
                h = t = p
                t.next = None
            else:
                p.next = h
                h = p
            
            p = self.h
        
        self.h = h
        self.t = t

    def reverseKGroup(self, head, k):
        if head == None or head.next == None or k < 2:
            return head
        cnt = 0
        h = t = None
        while head != None:
            self.h = self.t = None
            if head == None: 
                cnt = 0
            else:
                cnt = 0
                p = head
                while cnt < k and p != None:
                    head = head.next
                    if self.t == None:
                        self.h = self.t = p
                    else:
                        self.t.next = p
                        self.t = p

                    self.t.next = None
                    cnt += 1
                    p = head

            if cnt >= k:
                self.reverseList()
            if t == None:
                h = self.h
            else:
                t.next = self.h
            
            t = self.t
        
        head = h
        return head

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)

a1.next = a2
a2.next = a3

s = Solution()
res = s.reverseKGroup(a1, 2)

while res:
    print(res.val, end=" ")
    res = res.next