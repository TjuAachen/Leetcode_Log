class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        n = len(digits)
        final = []
        def backtracking(start, cur):
            if start == n:
                final.append(''.join(cur))
                return
            for i in mapping[digits[start]]:
                cur.append(i)
                backtracking(start+1,cur)
                cur.pop()
        backtracking(0,[])
        if n == 0:
            return []
        return final
                
                
        