class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse_word(l, r):
            while(l < r):
                s[l], s[r] = s[r], s[l]
                l = l + 1
                r = r - 1
        left, right = 0, len(s) - 1
        reverse_word(left, right)
        begin = 0
        while(begin <= right):
            end = begin
            while(end < right and s[end + 1] != " "):
                end += 1
            reverse_word(begin, end)
            begin = end + 2
        
        
            
            
            
            
        