class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        temp = None
        if not nums:
            return []
        def range2str(temp):
            if temp[0] == temp[1]:
                return str(temp[0])
            else:
                return '->'.join([str(num) for num in temp])
        for num in nums:
            if not temp:
                temp = [num,num]
            elif num - temp[1] == 1:
                temp.pop()
                temp.append(num)
            else:
                res.append(range2str(temp))
                temp = [num, num]
        res.append(range2str(temp))
        return res
                    
        