class Solution:
    def isInterleave(self, s1, s2, s3):
        n1 = len(s1)
        n2 = len(s2)
        if n1 + n2 != len(s3): return False
        if sorted(list(s1)+list(s2)) != sorted(list(s3)): return False
        res = [[False for col in range(n2+1)] for row in range(n1+1)]
        # res[0][0] = True
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 and j == 0:
                    res[i][j] = True
                elif i == 0:
                    res[i][j] = res[i][j-1] and (s2[j-1]==s3[j-1])
                elif j == 0:
                    res[i][j] = res[i-1][j] and (s1[i-1]==s3[i-1])
                else:
                    res[i][j] = (res[i][j-1] and (s2[j-1]==s3[i+j-1])) or (res[i-1][j] and (s1[i-1]==s3[i+j-1]))
        
        return res[n1][n2]