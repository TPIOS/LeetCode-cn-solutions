class Solution:
    def __init__(self):
        self.pos = list()
        self.n = self.m = 0
        self.flag = False
        self.l = 0
        self.target = ""
        self.direction = [[1,0],[-1,0],[0,1],[0,-1]]
    def search(self, board, x, y, s):
        if s == self.target: self.flag = True; return
        if len(s) >= self.l: return
        self.pos[x][y] = True
        for d in self.direction:
            if 0 <= x+d[0] <= self.n-1 and 0 <= y+d[1] <= self.m-1 and not self.pos[x+d[0]][y+d[1]] and board[x+d[0]][y+d[1]] == self.target[len(s)]:
                self.search(board, x+d[0], y+d[1], s+board[x+d[0]][y+d[1]])
                if self.flag: return
        self.pos[x][y] = False

    def exist(self, board, word):
        self.n = len(board)
        if self.n == 0: return False
        self.m = len(board[0])
        if self.m == 0: return False
        self.l = len(word)
        if self.l == 0 or self.l > self.n*self.m: return False
        self.target = word
        self.pos = [[False for col in range(self.m)] for row in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:
                    self.search(board,i,j,board[i][j])
        
        return self.flag

s = Solution()
print(s.exist(
    [
        ["b","a","a","b","a","b"],
        ["a","b","a","a","a","a"],
        ["a","b","a","a","a","b"],
        ["a","b","a","b","b","a"],
        ["a","a","b","b","a","b"],
        ["a","a","b","b","b","a"],
        ["a","a","b","a","a","b"]
    ],
        "aabbbbabbaababaaaabababbaaba")
    )