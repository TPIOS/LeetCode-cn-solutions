class Solution:
    def spiralOrder(self, matrix):
        res = []
        n = len(matrix)
        if n == 0: return []
        m = len(matrix[0])
        flag =  [[False for col in range(m)] for row in range(n)]
        cnt = 1
        dead_flag = False
        up, down, left, right = False, False, False, False
        row = 0
        column = 0
        while cnt != n*m+1:
            if not dead_flag:
                res.append(matrix[row][column])
                flag[row][column] = True
                cnt = cnt+1
            else:
                dead_flag = False

            if column+1 >= m or flag[row][column+1] or (down or left or up):
                right = False
                if row+1 >= n or flag[row+1][column] or (right or left or up):
                    down = False
                    if column-1 < 0 or flag[row][column-1] or (down or right or up):
                        left = False
                        if row-1 < 0 or flag[row-1][column] or (down or left or right):
                            up = False
                            dead_flag = True
                        else:
                            row = row - 1
                            up = True
                            down, left, right = False, False, False
                    else:
                        column = column - 1
                        left = True
                        down, up, right = False, False, False
                else:
                    row = row + 1
                    down = True
                    up, left, right = False, False, False
            else:
                column = column + 1
                right = True
                down, left, up = False, False, False 

        return res
    
s = Solution()
print(s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))