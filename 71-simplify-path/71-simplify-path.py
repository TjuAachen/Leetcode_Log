class Solution:
    def simplifyPath(self, path: str) -> str:
        ind = 0
        n = len(path)
        final = []
        def convert(s,ind):
            cancon = []
            slash = []
            while(ind < n):
                cur = s[ind]
                
                match cur:
                    case "/":
                        if ind == 0:
                            cancon.append(cur)
                            slash.append(len(cancon)-1)
                            ind = ind + 1                            
                        elif (s[ind-1] != "/" and (not cancon or cancon[-1] != '/')) and (ind != n - 1 or not cancon):
                            cancon.append(cur)
                            slash.append(len(cancon)-1)
                            ind = ind + 1
                        else:
                            ind = ind + 1
                    case ".":
                        count = 0
                        p = ind
                        while(ind < n and s[ind] == '.'):
                            count += 1
                            ind = ind + 1
                        if count > 2:
                            cancon.append('.'*count)
                        if count == 2 and (ind == n or s[ind] =='/') and (cancon and cancon[-1] =='/'):
                            if len(cancon) >= 3:
                                if len(slash) > 2:
                                    cancon = cancon[:slash[-2]]
                                    slash = slash[:-2]
                                else:
                                    cancon =['/']
                                    slash = [0]
                        elif count<=2 and (ind < n and s[ind] !='/'):
                            cancon.append('.'*count)
                        elif count <=2 and (cancon and cancon[-1] !='/'):
                            cancon.append('.'*count)
                    case _:
                        cancon.append(cur)
                        ind = ind + 1
            if len(cancon) > 1 and cancon[-1] == '/':
                cancon = cancon[:-1]
            result = ''.join(cancon)
            return result
        #convert(path,0,len(path),[])
        return convert(path,0)
                    
                    
            
        