class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hash_array = [0] * 26
        for char in s:
            hash_code = ord(char) - ord('a')
            hash_array[hash_code] += 1
        count = 0
        for num in hash_array:
            if num%2 != 0:
                count += 1
            if count > 1:
                return False
        return True
        