# import re
# class Solution:
#     def isMatch(self, s, p):
#         res = re.match(p, s)
#         if not res: return False
#         if res.group() == s:
#             return True
#         else:
#             return False

# a = Solution()
# print(a.isMatch('mismis','\[m.s]*'))

# class Solution:
#     def isMatch(self, s, p):
#         p_list = list()
#         ri = list()
#         rj = list()
#         s_len = len(s)
#         p_len = len(p)
#         i, j = 0, 0
#         while i < s_len or j < p_len:
#             if j + 1 < p_len and p[j+1] == "*":
#                 p_list.append(p[j])
#                 ri.append(i)
#                 j += 2
#                 rj.append(j)
#             elif i < s_len and j < p_len and (p[j] == "." or s[i] == p[j]):
#                 i += 1
#                 j += 1
#             elif len(p_list) != 0:
#                 k = ri[-1]
#                 if k < s_len and (p_list[-1] == "." or p_list[-1] == s[k]):
#                     k += 1
#                     i = k
#                     ri[-1] = k
#                     j = rj[-1]
#                 else:
#                     p_list.pop()
#                     ri.pop()
#                     rj.pop()
#             else:
#                 break
            
#         return (i == s_len and j == p_len)

# class Solution:
#     def isMatch(self, s, p):
#         s_len = len(s)
#         p_len = len(p)
#         d = [[False for col in range(p_len+1)] for row in range(s_len+1)]
#         d[0][0] = True
#         for i in range(s_len+1):
#             for j in range(1, p_len+1):
#                 if j > 1 and p[j-1]=="*":
#                     d[i][j] = d[i][j-2] or (i!=0 and d[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
#                 else:
#                     d[i][j] = i!=0 and d[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1]=='.')

#         return d[s_len][p_len]

class Solution:
    def isMatch(self, s, p):
        s_len = len(s)
        dp = [False]*(s_len+1)
        dp[s_len] = True
        i = len(p) - 1
        while i >= 0:
            if p[i] == '*':
                for j in range(s_len-1, -1, -1):
                    dp[j] = dp[j] or (dp[j + 1] and (p[i - 1] == '.' or p[i - 1] == s[j]))
                i -= 1
            else:
                for j in range(s_len):
                    dp[j] = dp[j + 1] and (p[i] == '.' or p[i] == s[j])
                dp[s_len] = False
            i -= 1

        return dp[0]

s = Solution()
print(s.isMatch("aaa","a*a"))