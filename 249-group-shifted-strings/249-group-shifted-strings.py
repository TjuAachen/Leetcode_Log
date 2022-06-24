class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        record = {}
        def shift_back(string):
            string = list(string)
            res = []
            step = ord(string[0]) - ord('a')
            for char in string:
                if ord('a') <= ord(char) - step <= ord('z'):
                    res.append(chr(ord(char)-step))
                else:
                    res.append(chr(ord(char)+(-step)%26))
            return ''.join(res)
        for string in strings:
            standard_key = shift_back(string)
            cur = record.setdefault(standard_key, [])
            cur.append(string)
        return list(record.values())