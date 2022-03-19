class Solution:
    def convert(self, s: str, numRows: int) -> str:
        number =[x for x in range(numRows-1,-1,-1)]
        back = []
        record = {}
        popped = -1
        n = len(s)
        index = 0
        while(index < n):
            char = s[index]
            if number[-1] != popped or numRows == 1:
                if number[-1] not in record:
                    record[number[-1]] = [char]
                else:
                    record[number[-1]].append(char)
                index = index + 1
            popped = number.pop()
            back.append(popped)
            if not number:
                number[:] = back[:]
                back = []
        result  = []
        for i in range(len(record)):
            result += record[i]
        return ''.join(result)
            
        