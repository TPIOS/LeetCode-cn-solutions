class Solution:
    def minWindow(self, s, t):
        ls = len(s)
        lt = len(t)
        if lt == 0 or ls < lt: return ""
        cnt = 0
        vs = [0] * 256
        vt = [0] * 256
        for i in range(lt):
            vt[ord(t[i])] += 1
            cnt += 1
        
        min_len = ls + 1
        res = ""
        j = 0
        for i in range(ls):
            if vs[ord(s[i])] < vt[ord(s[i])]: cnt -= 1
            vs[ord(s[i])] += 1
            if cnt > 0: continue
            
            ch = s[j]
            vs[ord(ch)] -= 1
            j += 1

            while vs[ord(ch)] >= vt[ord(ch)]:
                ch = s[j]
                vs[ord(ch)] -= 1
                j += 1
            
            cnt += 1

            if i-j+2 < min_len:
                min_len = i - j + 2
                res = s[j-1: j + min_len - 1]
        
        return res

s = Solution()
print(s.minWindow(s = "ADOBECODEBANCN", t = "ABC"))