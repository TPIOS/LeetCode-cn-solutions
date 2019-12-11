class Solution:
    def __init__(self):
        self.res = []
        self.puzzle = []

    def display(self, queen_num):
        tmp_res = []
        for i in range(0, queen_num):
            k = self.puzzle[i]
            tmp_row = k*'.'+'Q'+(queen_num-k-1)*'.'
            tmp_res.append(tmp_row)
        self.res.append(tmp_res)

    def judge(self, s):
        for i in range(0,s):
            if self.puzzle[i] == self.puzzle[s] or abs(self.puzzle[i]-self.puzzle[s]) == abs(i-s):
                return False
        return True

    def queen(self, x, queen_num):
        for i in range(0, queen_num):
            self.puzzle[x] = i
            if self.judge(x):
                if x == queen_num-1:
                    self.display(queen_num)
                else:
                    self.queen(x+1, queen_num)

    def solveNQueens(self, n):
        self.puzzle = [0]*n
        self.queen(0,n)
        return self.res

s = Solution()
print(s.solveNQueens(4))