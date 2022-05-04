class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        def combine(temp,root,nxt):
            n = len(nxt)
            for i in range(n):
                temp.append([root]+nxt[i])
                
        def generate(s,n):
            if n == 3:
                if len(s) > 0 and ((int(s) <= 255 and s[0] != '0') or s == '0'):
                    return True,[[s]]
                else:
                    return False,None
            temp = []
            for i in range(3):
                if (i+1) > len(s) or int(s[:(i+1)]) > 255 or (s[0] == '0' and i>0):
                    continue
                nxt = generate(s[i+1:],n+1)
                if nxt[0]:
                    combine(temp,s[:(i+1)],nxt[1])
            return True,temp
        res = generate(s,0)[1]
        final = []
        for elem in res:
            final.append('.'.join(elem))
        return final
            
                
            
        