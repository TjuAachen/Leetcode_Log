class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        record = dict()
        n = len(s)
        res = []
        if n < 10:
            return []
        for i in range(n - 9):
            substring = s[i:i+10]
            if substring in record and record[substring] == 1:
                res.append(substring)
                record[substring] += 1
            elif substring not in record:
                record[substring] = 1
        return res
        
                
            
        