class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = list(p)
        i = 0
        while(i < len(p)):
            j = i
            while(j < len(p) and p[j] == '*'):
                j = j + 1
            if i != j:
                p = p[:i+1] + p[j:]
            i = i + 1
        p = ''.join(p)
        record = dict()
        def find(s, p, i, j):
            #termination conditions
            if (i,j) in record:
                return record[(i,j)]
            if (i == len(s) and j == len(p)) or (j==len(p)-1 and i==len(s) and p[j] == '*'):
                return True
            if (i == len(s) or j == len(p)):
                return False
            if p[j] == "?":
                if (i+1,j+1) not in record:
                    record[(i+1,j+1)] = find(s, p, i+1, j+1)
                return record[(i+1,j+1)]
            elif p[j] == "*":
                if (i+1,j) not in record:
                    record[(i+1,j)] = find(s,p,i+1,j)
                if (i,j+1) not in record:
                    record[(i,j+1)] = find(s,p,i,j+1)
                return record[(i,j+1)] or record[(i+1,j)]
            elif s[i] == p[j]:
                if (i+1,j+1) not in record:
                    record[(i+1,j+1)] = find(s,p,i+1,j+1)              
                return record[(i+1,j+1)]
            else:
                record[(i,j)] = False
                return False
      #  return False
        return find(s,p,0,0)
                