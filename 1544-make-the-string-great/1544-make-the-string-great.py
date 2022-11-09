class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for i in s:
            if len(result) == 0:
                result.append(i)
            else:
                last = result.pop()
                if i==last or i.lower() != last.lower():
                    result.append(last)
                    result.append(i)
        return "".join(result)