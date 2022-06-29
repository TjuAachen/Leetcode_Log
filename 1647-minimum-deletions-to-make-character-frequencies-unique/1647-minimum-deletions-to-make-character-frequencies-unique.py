from collections import *
class Solution:
    def minDeletions(self, s: str) -> int:
        hash_array = [0] * 26
        for char in s:
            hash_code = ord(char) - ord('a')
            hash_array[hash_code] += 1
        
        min_val = float('inf')
        deleted = 0
        hash_array.sort(reverse = True)
        
        seen = set()
        delete_count = 0
        for i, num in enumerate(hash_array):
            while(num in seen and num > 0):
                delete_count += 1
                num -= 1
            if num not in seen:
                seen.add(num)
        return delete_count
        