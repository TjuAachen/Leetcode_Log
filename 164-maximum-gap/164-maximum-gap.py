class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        
        
        min_num, max_num = min(nums), max(nums)
        
        record = [0] * length
        
        deviation = min_num
        
        def hash_fun(num):
            if num == max_num:
                return length - 1
            return (num - deviation) * length // (max_num - deviation)
        
        for num in nums:
            index = hash_fun(num)
            if record[index] == 0:
                record[index] = [num, num]
            else:
                record[index] = [min(record[index][0], num),max(record[index][1], num)]
        ans = 0
        i = 0
        while(i < length):
            if i < length - 1 and record[i] != 0:
                j = i + 1
                while(j < length and record[j] == 0):
                    j = j + 1
                if j < length:
                    ans = max(ans, record[j][0] - record[i][-1])
                i = j
            else:
                i = i + 1
        return ans
            
        
            
        