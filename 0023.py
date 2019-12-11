import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        res_list = []
        for list_num in lists:
            while list_num != None:
                heapq.heappush(res_list, list_num.val)
                list_num = list_num.next
        
        res = ListNode(0)
        tmp = ListNode(0)
        res.next = tmp

        while res_list != []:
            cc = ListNode(heapq.heappop(res_list))
            tmp.next = cc
            tmp = cc
        
        return res.next.next

