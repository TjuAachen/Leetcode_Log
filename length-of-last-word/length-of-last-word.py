class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s[::-1].strip()
        subString = s.split(' ')
        return len(subString[0])
    
        