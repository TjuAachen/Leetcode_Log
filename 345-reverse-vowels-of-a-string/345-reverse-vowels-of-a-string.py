class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set(['a','e','i','o','u','A','E','I','O','U'])
        s = list(s)
        vowel_string = []
        vowel_position = []
        for i, char in enumerate(s):
            if char in vowel:
                vowel_position.append(i)
            #    vowel_string.append(char)
        
        n = len(vowel_position)
        
        for i in range(n//2):
            original_position = vowel_position[i]
            reversed_position = vowel_position[n-1-i]
            s[original_position], s[reversed_position] = s[reversed_position], s[original_position]
        return ''.join(s)
            