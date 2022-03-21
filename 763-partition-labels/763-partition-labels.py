class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        record = {}
        for index, char in enumerate(s):
            if char in record:
                record[char][1] = index
            else:
                record[char] = [index, index]
        start = 0
        end = record[s[0]][1]
        res = []
        for index,char in enumerate(s):
            new_end = record[char][1]
            if new_end > end:
                end = new_end
            if end == index:
                res.append(end-start+1)
                start = end + 1
        return res
            
                
        