class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n =len(s), len(t)
        count = dict()
        for char in t:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        left, right = 0, 0
        def equals(l1, l2):
            if not l1:
                return False
            for char,num in l2.items():
                if char not in l1:
                    return False
                if char in l1 and l1[char] < num:
                    return False
            return True
        cur = dict()
        res = ''
        while(right < m and left <= right):
            while(right<m and not equals(cur,count)): 
                if s[right] in cur:
                    cur[s[right]] += 1
                else:
                    cur[s[right]] = 1
                right = right+1
            while(left < right and equals(cur,count)):
                if cur[s[left]] > 1:
                    cur[s[left]] = cur[s[left]] - 1
                else:
                    del cur[s[left]]
                if (res == '' or right-left < len(res)):
                    res = s[left:right]
                left = left + 1
        return res
            
            
            
        
        