class Solution:
    def longestCommonPrefix(self, strs):
        '''
        if len(strs) == 0: return ""
        res = ""
        tmp_res = ""
        max_len = len(strs[0])
        idx = 0
        while idx < max_len:
            tmp_res += strs[0][idx]
            flag = True
            for s in strs:
                if s.find(tmp_res) == -1 or s.find(tmp_res) != 0:
                    flag = False
                    break
            if flag:
                res = tmp_res
                idx += 1
            else:
                return res

        return res
        '''

        if not strs:
            return ''
        strs.sort()
        res = ''
        for i in range(len(strs[0])):
            if strs[-1][i] != strs[0][i]:
                return res
            res += strs[0][i]
        return res

s = Solution()
print(s.longestCommonPrefix(["a","cc","acc"]))
                
