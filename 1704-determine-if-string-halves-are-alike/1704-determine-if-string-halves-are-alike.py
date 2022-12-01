class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        n = len(s)
        
        half = n // 2
        
        firstHalfVowel = 0
        secondHalfVowel = 0
        
        for i in range(half):
            if s[i].lower() in vowels:
                firstHalfVowel += 1
            
        
        for i in range(half, n):
            if s[i].lower() in vowels:
                secondHalfVowel += 1            
        
        
        return secondHalfVowel == firstHalfVowel
    
    