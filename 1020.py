class Solution:
    def dfsMain(self, grid, i, j, rowSize, colSize):
        if i < 0 or i >= rowSize: return
        if j < 0 or j >= colSize: return
        if grid[i][j] == 1:
            grid[i][j] = 0
            self.dfsMain(grid, i-1, j, rowSize, colSize) # up
            self.dfsMain(grid, i+1, j, rowSize, colSize) # down
            self.dfsMain(grid, i, j+1, rowSize, colSize) # right
            self.dfsMain(grid, i, j-1, rowSize, colSize) #left

    def numEnclaves(self, grid):
        rowSize = len(grid)
        colSize = len(grid[0])
        # first row
        i = 0
        for j in range(colSize):
            if grid[i][j] == 1:
                grid[i][j] = 0
                self.dfsMain(grid, i-1, j, rowSize, colSize) # up
                self.dfsMain(grid, i+1, j, rowSize, colSize) # down
                self.dfsMain(grid, i, j+1, rowSize, colSize) # right
                self.dfsMain(grid, i, j-1, rowSize, colSize) #left
        # first column
        j = 0
        for i in range(rowSize):
            if grid[i][j] == 1:
                grid[i][j] = 0
                self.dfsMain(grid, i-1, j, rowSize, colSize) # up
                self.dfsMain(grid, i+1, j, rowSize, colSize) # down
                self.dfsMain(grid, i, j+1, rowSize, colSize) # right
                self.dfsMain(grid, i, j-1, rowSize, colSize) #left
        # last row
        i = rowSize - 1
        for j in range(colSize):
            if grid[i][j] == 1:
                grid[i][j] = 0
                self.dfsMain(grid, i-1, j, rowSize, colSize) # up
                self.dfsMain(grid, i+1, j, rowSize, colSize) # down
                self.dfsMain(grid, i, j+1, rowSize, colSize) # right
                self.dfsMain(grid, i, j-1, rowSize, colSize) #left
        # last column
        j = colSize - 1
        for i in range(rowSize):
            if grid[i][j] == 1:
                grid[i][j] = 0
                self.dfsMain(grid, i-1, j, rowSize, colSize) # up
                self.dfsMain(grid, i+1, j, rowSize, colSize) # down
                self.dfsMain(grid, i, j+1, rowSize, colSize) # right
                self.dfsMain(grid, i, j-1, rowSize, colSize) #left
        
        ans = 0
        for idx in grid:
            ans += sum(idx)
        return ans


a = Solution()
print(a.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))