def lengthOfLongestSubstring(s):
    if len(s) == 0: return 0
    substr = dict()
    idx = 0
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] in substr:
            idx = max(idx, substr.get(s[i]))
        substr[s[i]] = i+1
        ans = max(ans, i-idx+1)
    return ans

# def lengthOfLongestSubstring(self, s):
#         if len(s) == 0: return 0
#         d = []
#         substr = dict()
#         for i in range(len(s)):
#             if substr.get(s[i]):
#                 idx = substr.get(s[i])
#                 substr=dict()
#                 for j in range(idx+1, i):
#                     substr[s[j]] = j
#                 substr[s[i]] = i
#                 d.append(max(1,d[i-1]))
#             else:
#                 substr[s[i]] = i
#                 if i == 0: 
#                     d.append(1)
#                 else:
#                     d.append(max(d[i-1], len(substr)))

#         return d[len(s)-1]


print(lengthOfLongestSubstring('abcabcaa'))