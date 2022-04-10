class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for char in ops:
            if char == "C":
                record.pop()
            elif char == "D":
                record.append(record[-1]*2)
            elif char == "+":
                first = record[-1]
                second = record[-2]
                record.append(first+second)
            else:
                record.append(int(char))
        return sum(record)