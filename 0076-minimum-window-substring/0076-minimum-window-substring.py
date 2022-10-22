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
        required = len(target)
        formed = 0
        minString = ""
        while(right < n):
            curChar = s[right]
            curDict[curChar] += 1
            right += 1
            if curChar in target and curDict[curChar] == target[curChar]:
                formed += 1
            while(left < right and formed == required):
                curLeftChar = s[left]
                curDict[curLeftChar] -= 1
                if ans > right - left:
                    minString = s[left : right]
                    ans = right - left
                if curLeftChar in target and target[curLeftChar] > curDict[curLeftChar] :
                     formed -= 1
                left += 1
        return minString
            

        