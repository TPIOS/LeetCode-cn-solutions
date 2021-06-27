class Solution:
    def simplifyPath(self, path):
        res = []
        for part in path.split('/'):
            if part in {'.', ''}:
                continue
            if part == '..':
                if res:
                    res.pop()
            else:
                res.append(part)
                
        return '/'+ '/'.join(res)