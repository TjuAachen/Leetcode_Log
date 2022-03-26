class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        def combine(letters,output):
            new = []
            for letter in letters:
                for element in output:
                    new.append(element+letter)
            return new
        output =[""]
        for digit in digits:
            output = combine(mapping[digit],output)
        if digits == "":
            return []
        return output
            