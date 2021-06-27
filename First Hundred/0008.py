class Solution:
    def myAtoi(self, s):
        res = ""
        max_int = 0x7FFFFFFF
        min_int = -max_int-1
        flag = True
        for c in s:
            if c == ' ' and flag: continue
            if (c == '-' or c == '+') and flag: 
                res += c + '0'
                flag = False
                continue
            
            if not c.isdigit():
                if len(res) == 0: return 0
                if int(res) < min_int: return min_int
                if int(res) > max_int: return max_int
                return int(res)
            else:
                res += c
                flag = False
        
        if len(res) == 0: return 0
        if int(res) < min_int: return min_int
        if int(res) > max_int: return max_int
        return int(res)

s = Solution()
print(s.myAtoi('+-'))