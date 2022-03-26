class Solution:
    def romanToInt(self, s: str) -> int:
        record ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n = len(s) - 1
        prev = ["I","X","C"]
        final = 0
        for ind, char in enumerate(s):
            if char in prev:
                if ind < n and record[s[ind+1]]>record[char]:
                    final = final - record[char]
                else:
                    final += record[char]
            else:
                final += record[char]
        return final
        