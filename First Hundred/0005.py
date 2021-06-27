def init(s):
    s_new = ['$']
    for c in s:
        s_new.append('#')
        s_new.append(c)
    s_new.append('#')
    s_new.append('@')
    return s_new

def deal(idx, l, s):
    res = ""
    for i in range(idx-l+1, idx+l):
        if s[i] != "#": res += s[i]
    return res

def longestPalindrome(s):
    s_new = init(s)
    l = len(s_new)
    max_len = -1
    max_idx = -1
    mx = idx = 0
    p = list()

    for i in range(l-1):
        if i < mx:
            p.append(min(p[2*idx - i], mx-i))
        else:
            p.append(1)
        
        while s_new[i-p[i]] == s_new[i+p[i]]:
            p[i] += 1
        
        if mx < i+p[i]:
            idx = i
            mx = i+p[i]
        
        if max_len < p[i]-1:
            max_len = p[i]-1
            max_idx = i
    
    return deal(max_idx, max_len, s_new)
    

print(longestPalindrome('babad'))
