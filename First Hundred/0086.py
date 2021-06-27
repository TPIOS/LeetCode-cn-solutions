# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        if head == None: return head
        smallList = None
        bigList = None
        while head != None:
            if head.val < x:
                if smallList == None:
                    smallList = ListNode(head.val)
                    tmpSmallBigin = smallList
                else:
                    smallList.next = ListNode(head.val)
                    smallList = smallList.next
            else:
                if bigList == None:
                    bigList = ListNode(head.val)
                    tmpBigBigin = bigList
                else:
                    bigList.next = ListNode(head.val)
                    bigList = bigList.next

            head = head.next
        
        if smallList != None:
            if bigList != None:
                smallList.next = tmpBigBigin
            res = tmpSmallBigin
        else:
            res = tmpBigBigin
        
        return res        