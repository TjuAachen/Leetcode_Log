class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        old_hash = - 1
        count = (1<<k)
        all_one = (1<<k) - 1
        hash_table = [0] * (1<<k)
        def str2bin(string):
            res = 0
            for char in string:
                res = res * 2+ int(char)
            return res
        for i in range(n - k + 1):
            if count == 0:
                return True
            substring = s[i:(i+k)]
            if old_hash == -1:
                new_hash = str2bin(substring)
            else:
                new_hash = ((old_hash << 1) & all_one) | int(substring[-1])
            if hash_table[new_hash] == 0:
                count = count - 1
                old_hash = new_hash
                hash_table[new_hash] = 1
            else:
                old_hash = new_hash
        if count == 0:
            return True
        return False
                
            