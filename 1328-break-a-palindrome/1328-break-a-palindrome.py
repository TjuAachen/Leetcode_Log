class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        #input : a palindromic string
        #output : a non-palindromic string 
        #breaking down the problem:
        #1. traverse from the beginning
        #2. for each character, if it is 'a', then move to the next
        #if it is not 'a', then change it to 'a', return the result
        sList = []
        totalLen = len(palindrome)
        n = len(palindrome) // 2
        hasChanged = False
        isEven = totalLen%2 == 0
        if n == 0:
            return ""
        for i in range(totalLen):
            curChar = palindrome[i]
            if curChar == 'a':
                if i == totalLen - 1 and not hasChanged:
                    sList.append('b')
                else:
                    sList.append('a')
            else:
                if isEven and not hasChanged:
                    hasChanged = True
                    sList.append('a')
                elif not isEven and not hasChanged and i != n:
                    hasChanged = True
                    sList.append('a')
                else:
                    sList.append(curChar)
        return ''.join(sList)