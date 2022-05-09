class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        n = len(digits)
        path = []
        result = []
        #backtracking
        def generate(stage):
            if stage == n:
                if path:
                    result.append(''.join(path))
                return
            #make choices
            for char in mapping[digits[stage]]:
                path.append(char)
                generate(stage+1)
                path.pop()
        generate(0)
        return result
            
                
                
        