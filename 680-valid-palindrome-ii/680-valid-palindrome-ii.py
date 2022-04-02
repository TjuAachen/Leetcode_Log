class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validate(s, num):
            left, right = 0, len(s) - 1
            while(left < right):
                if num < 1 and s[left] != s[right]:
                    num += 1
                    if validate(s[left+1:right+1],num) or validate(s[left:right],num):
                        return True
                    else:
                        return False
                elif num >=1 and s[left]!=s[right]:
                    return False
                else:
                    left, right = left + 1, right - 1
            return True
        return validate(s,0)
        