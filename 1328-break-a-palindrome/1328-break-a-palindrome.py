class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        #input : a palindromic string
        #output : a non-palindromic string 
        #breaking down the problem:
        #1. traverse from the beginning
        #2. for each character, if it is 'a', then move to the next
        #if it is not 'a', then change it to 'a', return the result
        totalLen = len(palindrome) 
        n = totalLen // 2
        if n == 0:
            return ""
        for i in range(n):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'