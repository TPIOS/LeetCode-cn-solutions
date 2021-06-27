class Solution:
    def convert(self, s, numRows):
        if numRows == 1: return s

        res = ""
        max_inc = (numRows-1)*2
        idx = tmp = 0
        l = len(s)

        while tmp < l:
            res += s[tmp]
            tmp += max_inc

        for k in range(max_inc-2,0,-2):
            idx += 1
            tmp = idx
            left = max_inc - k
            while tmp < l:
                res += s[tmp]
                if tmp + k < l:
                    tmp += k
                    res += s[tmp]
                else:
                    break
                tmp += left
        
        idx += 1
        tmp = idx
        while tmp < l:
            res += s[tmp]
            tmp += max_inc

        return res

s = Solution()
print(s.convert('ABCD',4))
                
