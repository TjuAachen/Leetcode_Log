class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        res = []
        for query in queries:
            temp = 0
            for size in range(1+n):
                cur_sum = prefix_sum[size]
                if cur_sum <= query:
                    temp = max(temp, size)
            res.append(temp)
        
        return res