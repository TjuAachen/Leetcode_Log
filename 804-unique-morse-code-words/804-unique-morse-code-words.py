class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        final=set()
        for word in words:
            result=""
            for i in word:
                result=result+mos[ord(i)-97]
            final.add(result)
        return len(final)
        