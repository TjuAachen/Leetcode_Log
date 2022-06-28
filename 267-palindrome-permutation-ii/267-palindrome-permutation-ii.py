class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        #decide whether it can generate palindromes
        hash_array = [0] * 26
        count = 0
        for char in s:
            index = ord(char) - ord('a')
            hash_array[index] += 1
        odd = -1
        possible = []
        for i, num in enumerate(hash_array):
            if num%2 != 0:
                count += 1
                odd = i
            if num != 0:
                temp = [chr(ord('a')+i)]*(num//2)
                possible.extend(temp)
            if count > 1:
                return []
        s_len = len(s)
        middle = ''
        if s_len%2 != 0:
            middle = chr(odd + ord('a'))
        temp_res = []
        visited = set()
        res = []
        def permutation(num):
            if num == s_len//2:
                cur = temp_res[:]
                cur = cur + [middle] + cur[::-1]
                res.append(''.join(cur[:]))
                return
            for i, choice in enumerate(possible):
                if i in visited:
                    continue
                if i > 0 and possible[i-1] == possible[i] and i-1 not in visited:
                    continue
                temp_res.append(choice)
                visited.add(i)
                permutation(num+1)
                temp_res.pop()
                visited.remove(i)
        permutation(0)
        return res