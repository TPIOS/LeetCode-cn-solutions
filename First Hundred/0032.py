# class Solution:
#     def longestValidParentheses(self, s):
#         res = 0
#         p = list()
#         for i in range(len(s)):
#             if s[i] == '(':
#                 p.append(s[i])
#             else:
#                 if len(p) == 0: continue
#                 if p[-1] == '(':
#                     if len(p) == 1:
#                         p.pop()
#                         p.append(str(2))
#                     else:
#                         tmp = 2
#                         p.pop()
#                         while len(p) > 0 and p[-1].isdigit(): tmp += int(p.pop())
#                         p.append(str(tmp))
#                 elif p[-1].isdigit():
#                     if len(p) == 1:
#                         res = max(res, int(p[-1]))
#                         p = list()
#                     else:
#                         tmp = int(p.pop()) + 2
#                         p.pop()
#                         while len(p) > 0 and p[-1].isdigit(): tmp += int(p.pop())
#                         p.append(str(tmp))

#         for c in p:
#             if c.isdigit():
#                 res = max(res, int(c))

#         return res

# s = Solution()
# print(s.longestValidParentheses(")(((((()())()()))()(()))("))

class Solution:
    def longestValidParentheses(self, s):
        max_len = 0
        dp = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                dp.append(i)
            else:
                dp.pop()
                if(len(dp) == 0):
                    dp.append(i)
                else:
                    max_len = max(max_len, i - dp[-1])
                    
        return max_len