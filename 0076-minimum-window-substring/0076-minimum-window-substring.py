class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right = 0, 0
        target = Counter(t)
        n = len(s)
        ans = float('inf')
        curDict = defaultdict(int)
        minString = ""
        while(right < n):
            curChar = s[right]
            curDict[curChar] += 1
            right += 1
            while(self.isIncluded(curDict, target) and left < right):
                curLeftChar = s[left]
                curDict[curLeftChar] -= 1
                if ans > right - left:
                    minString = s[left : right]
                    ans = right - left
                left += 1
        return minString
            
        
    
    def isIncluded(self, curDic, target):
        for char, freq in target.items():
            if char not in curDic or curDic[char] < freq:
                return False
        return True
        