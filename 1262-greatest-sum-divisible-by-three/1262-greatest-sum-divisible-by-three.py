class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        record = defaultdict(list)
        for num in nums:
            record[num%3].append(num)
        n1, n2 = len(record[1]), len(record[2])
        record[1].sort()
        record[2].sort()
        ans = sum(nums)
        
        status = ans%3
        possible = 0
        if status == 0:
            return ans
        if record[status]:
            possible = max(possible,ans - record[status][0])
        if status == 1:
            if len(record[2])>1:
                possible = max(possible,ans - record[2][0] - record[2][1])
        if status == 2:
            if len(record[1])>1:
                possible=max(possible,ans - record[1][0] - record[1][1])
         
        return possible
        
            
        
        