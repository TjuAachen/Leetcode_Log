class Solution:
    def longestPalindrome(self, s: str) -> str:
        #preprocessing
        s_length = len(s)
        s_post = []
        for i, char in enumerate(s):
            s_post.append('#')
            s_post.append(char)
        s_post.append('#')
        newS_length = len(s_post)
        
        maxRight, center = 0, 0
        i = 0
        maxLen = 0
        p = [0] * newS_length
        while(i < newS_length):
            if i <= maxRight:
                mirror = 2 * center - i
                p[i] = min(p[mirror], maxRight - i)
            left = i - p[i] - 1
            right = i + p[i] + 1
            while(left >= 0 and right < newS_length and s_post[left] == s_post[right]):
                left = left - 1
                right += 1
                p[i] += 1
                
            #update maxRight
            if i + p[i] > maxRight:
                maxRight = i + p[i]
                center = i
            
            if p[i] > maxLen:
                maxLen = p[i]
                start = (i - maxLen) // 2
            i = i + 1
        return s[start:start+maxLen]
        
    
                    
        
            