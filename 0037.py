class Solution(object):
    def __init__(self):
        self.finish = False

    def isvaild(self, board, i, j):  
            for m in range(9):  
                if m!=i and board[m][j]==board[i][j]:  
                    return False  
            for n in range(9):  
                if n!=j and board[i][n]==board[i][j]:  
                    return False  
            for m in range(i//3*3,i//3*3+3):  
                for n in range(j//3*3,j//3*3+3):  
                    if m!=i and n!=j and board[m][n]==board[i][j]:  
                        return False  
            return True

    def checkFinish(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    return False
        return True

    def solveSudoku(self, board):
        if self.finish: return
        
        if self.checkFinish(board):
            self.finish = True
            return

        for i in range(9):  
            for j in range(9):  
                if board[i][j]=='.':  
                    for c in '123456789':  
                        board[i][j] = c  
                        if self.isvaild(board,i,j):  
                            self.solveSudoku(board)
                            if self.finish: return 
                        board[i][j] = '.' 

                    return 