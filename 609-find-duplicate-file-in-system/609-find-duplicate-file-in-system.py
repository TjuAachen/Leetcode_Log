class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        self.contentToPath = defaultdict(list)
        
        for path in paths:
            self.parsePath(path)
        
        res = []
        for key, value in self.contentToPath.items():
            if len(value) > 1:
                res.append(value)
        return res
        
    
    def parsePath(self,path):
        pathArray= path.split(' ')
        
        filePath = pathArray[0]
        
        n = len(pathArray)
        
        for i in range(1, n):
            txtPath, curTxt = self.parseContent(pathArray[i])
            self.contentToPath[curTxt].append(filePath +'/' +txtPath)
            
    
    def parseContent(self, txt):
        res = ''
        for i in range(len(txt) - 2, -1, -1):
            curChar = txt[i]
            if curChar == '(':
                break
            else:
                res = curChar + res
        return txt[:i], res
        
                
                
            
            
            
        
        
        
        
        