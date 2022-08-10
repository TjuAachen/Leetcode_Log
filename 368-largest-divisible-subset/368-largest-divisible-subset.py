class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        factors = defaultdict(list)
      #  prev = None
        for i, num in enumerate(nums):
            for j in range(i-1,-1,-1):             
                if num%nums[j] == 0:
                    factors[num] = factors[nums[j]][:]
                    break
            factors[num].append(num)
        visited = set()
        res = []
        
        best_res = defaultdict(list)
        n = len(nums)
        best_res[nums[0]].append(nums[0])
        final_len = 1
        final_set = [nums[0]]
        for i in range(1, n):
            cur = nums[i]
            max_len = 0
            max_subset = None
            for j in range(i):
                if cur%nums[j] == 0 and len(best_res[nums[j]]) > max_len:
                    max_len = len(best_res[nums[j]])
                    max_subset = best_res[nums[j]]
            if max_subset:
                best_res[cur] = max_subset[:]
            best_res[cur].append(cur)
            if len(best_res[cur]) > final_len:
                final_set = best_res[cur]
                final_len = len(best_res[cur])
        return final_set