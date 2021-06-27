from copy import deepcopy
class Solution:
    def __init__(self):
        self.ans = []
    def dfsMain(self, k, n, tmp):
        if n <= 0:
            return
        if k == 1:
            if n in tmp:
                return
            if n > 9:
                return
            tmp.append(n)
            if sorted(tmp) not in self.ans:
                self.ans.append(sorted(tmp))
            # print(self.ans)
            return
        start = tmp[-1]
        # print(n, start)
        for i in range(start+1, 10):
            tmp.append(i)
            # print("before:", tmp)
            self.dfsMain(k-1, n-i, deepcopy(tmp))
            # print("after:", tmp)
            tmp.pop()
   
    def combinationSum3(self, k, n):
        for i in range(1, 10):
            self.dfsMain(k-1,n-i,deepcopy([i]))
        return self.ans

a = Solution()
a.combinationSum3(2,18)
print(a.ans)