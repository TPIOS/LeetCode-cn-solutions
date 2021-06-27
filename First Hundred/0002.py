class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    tmp = l1
    while l1.next:
        if l2:
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        else:
            l1 = l1.next
    
    if l2:
        l1.val += l2.val
        l1.next = l2.next
    
    res = tmp
    p = 0
    while tmp.next:
        tmp.val += p
        p = tmp.val // 10
        tmp.val %= 10
        tmp = tmp.next
        
    tmp.val += p
    p = tmp.val // 10
    tmp.val %= 10

    if p:
        tmp.next = ListNode(p)
    
    return res

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)

a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
# b4 = ListNode(4)

b1.next = b2
b2.next = b3
# b3.next = b4

res = addTwoNumbers(a1, b1)
while res:
    print(res.val, end=" ")
    res = res.next