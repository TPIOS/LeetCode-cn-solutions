class Solution:
    def check(self, nums):
        tmp = {}
        for num in nums:
            if num.isdigit():
                if num in tmp:
                    return False
                else:
                    tmp[num] = 1
        return True

    def isValidSudoku(self, board):
        for row in board:
            if not self.check(row): return False

        for i in range(0,9):
            col = list()
            for row in board:
                col.append(row[i])
            if not self.check(col): return False
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                grid = list()
                for i1 in range(0,3):
                    for j1 in range(0,3):
                        grid.append(board[i+i1][j+j1])
                if not self.check(grid): return False
        
        return True

s = Solution()
print(s.isValidSudoku(board = [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]))