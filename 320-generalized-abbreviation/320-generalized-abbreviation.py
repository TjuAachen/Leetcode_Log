class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        seen = set()
        visited = set()
        def abbreviate(string):
            i = 0
            res = []
            while(i < n):
                count = 0
                j = i
                while(j < n and string[j] == '*'):
                    count += 1
                    j = j + 1
                if count != 0:
                    res.append(str(count))
                else:
                    res.append(string[i])
                i = max(j, i + 1)
            return ''.join(res)
        ans = []
        
        def modify(cur_index, cur_string):
            if (cur_index, cur_string) in visited:
                return
            if cur_string not in seen:
                ans.append(abbreviate(cur_string))
                seen.add(cur_string)
            if cur_index == n:
                return
            visited.add((cur_index, cur_string))
            for i in range(cur_index, n):
                temp = cur_string[:i] + '*' + cur_string[i+1:]
                modify(i+1, temp)
                
                modify(i+1, cur_string)
        modify(0, word)
        
        return ans
            
            