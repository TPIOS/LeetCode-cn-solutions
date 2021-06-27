# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        if head == None or m == n: return head
        return_head = None
        record_head = None
        tail = None
        one_node_before_tail = None
        cnt = 1
        flag = False
        while head != None:
            if cnt < m:
                if return_head == None and record_head == None:
                    return_head = record_head = head
                record_head = head
                head = head.next
            elif cnt == m:
                tail = one_node_before_tail = head
                head = head.next
                tail.next = None
                one_node_before_tail.next = None
            elif cnt <= n:
                tmp_node = head
                head = head.next
                tmp_node.next = one_node_before_tail
                one_node_before_tail = tmp_node
            else:
                flag = True
                if record_head == None:
                    return_head = record_head = one_node_before_tail
                else:
                    record_head.next = one_node_before_tail
                tail.next = head
                break
        
            cnt += 1
        
        if not flag:
            if record_head == None:
                return_head = record_head = one_node_before_tail
            else:
                record_head.next = one_node_before_tail

        return return_head

