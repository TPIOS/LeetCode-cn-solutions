class Solution:
    def __init__(self):
        self.ans = []
    def dfsMain(self, num, target, expression):
        if num == "":
            if eval(expression) == target:
                self.ans.append(expression)
        else:
            for i in range(1, len(num)+1):
                if i > 1 and num[0] == "0": break
                # cur = eval(num[:i])
                self.dfsMain(num[i:], target, expression+'+'+num[:i])
                self.dfsMain(num[i:], target, expression+'-'+num[:i])
                self.dfsMain(num[i:], target, expression+'*'+num[:i])


    def addOperators(self, num, target):
        for i in range(1, len(num)+1):
            if i > 1 and num[0] == "0": break
            self.dfsMain(num[i:], target, num[:i])
        return self.ans

a = Solution()
a.addOperators("3456237490",8)
print(a.ans)