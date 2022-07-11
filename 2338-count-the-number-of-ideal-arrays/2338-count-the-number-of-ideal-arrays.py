class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        record = defaultdict(list)
        def num_of_factors(num):
            maximum = int(math.sqrt(num))
            i = 1
            ans = 0
            temp = set()
            while(i <= maximum):
                if num%i == 0:
                    if i not in temp:
                        ans += 1
                        record[num-1].append(i-1)
                        temp.add(i)
                    if num//i not in temp:
                        ans += 1
                        record[num-1].append(num//i-1)
                        temp.add(num//i)
                i += 1
        dp = [0 for _ in range(maxValue)]
        for i in range(1,maxValue + 1):
            dp[i-1] = num_of_factors(i)

        maximum_length = min(n,int(math.log(maxValue)/math.log(2))+1)
        
        count = [[1 for _ in range(maxValue)] for _ in range(maximum_length + 1)]
        
        count_by_length = [0 for _ in range(maximum_length + 1)]
        count_by_length[0] = maxValue
        for i in range(1, maximum_length + 1):
            for j in range(maxValue):
                count[i][j] = 0
                for prev in record[j]:
                    if count[i-1][prev] != 0 and prev != j:
                        count[i][j] += count[i-1][prev]
                count_by_length[i] += count[i][j]
        ans = 0
        for i in range(maximum_length + 1):
            ans += math.comb(n-1, i) * count_by_length[i]
        return ans%(10**9+7)
            
            
            
        
        