class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        record = dict()
        target = ''.join(sorted(words))
        length = len(words[0])
        num = len(words)
        index = 0
        output = []
        while(index < len(s)-num*length + 1):
            partition = s[index:index+num*length]
            chunks = [partition[i:i+length] for i in range(0, len(partition), length)]
            
            chunks = ''.join(sorted(chunks))
            if chunks == target:
                output.append(index)
            index = index + 1

            
        return output
            
            