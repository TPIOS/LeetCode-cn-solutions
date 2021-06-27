class Solution:
    def restoreIpAddresses(self, s):
        n = len(s)
        res = []
        tmp = []
        for i in range(1,1+3):
            if i > n: break
            if len(s[0:i]) != len(str(int(s[0:i]))): break
            if int(s[0:i]) > 255: break
            tmp.append(s[0:i])
            for j in range(i+1,i+4):
                if j > n: break
                if len(s[i:j]) != len(str(int(s[i:j]))): break
                if int(s[i:j]) > 255: break
                tmp.append(s[i:j])
                for k in range(j+1,j+4):
                    if k >= n: break
                    if len(s[j:k]) != len(str(int(s[j:k]))): break
                    if int(s[j:k]) > 255: break
                    tmp.append(s[j:k])

                    if len(s[k:]) > 3: tmp.pop();continue
                    if len(s[k:]) != len(str(int(s[k:]))): tmp.pop();continue
                    if int(s[k:]) > 255: tmp.pop();continue
                    
                    tmp.append(s[k:])
                    res.append(".".join(tmp))

                    tmp.pop()
                    tmp.pop()
                tmp.pop()
            tmp.pop()
        
        return res

s = Solution()
print(s.restoreIpAddresses("110515"))


