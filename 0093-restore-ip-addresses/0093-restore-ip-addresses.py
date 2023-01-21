class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        
        self.recursion(0, "", s, 0, ans)
        
        return ans
        
        
    def recursion(self, step, curRes, s, start, ans):
        n = len(s)
        if step == 3:
            curStr = s[start:]
            if start < n and int(curStr) <= 255:
                if len(curStr) > 1 and curStr[0] == "0":
                    return
                curRes += '.' + curStr
                ans.append(curRes)
            return
        curVal = ""
        for idx in range(start, n):
            curVal += s[idx]
            if len(curVal) > 1 and curVal[0] == "0":
                continue
            if int(curVal) <= 255:
                if len(curRes) == 0:
                    temp = curVal
                else:
                    temp = curRes +"." + curVal
                self.recursion(step + 1, temp, s, idx + 1, ans)
        return