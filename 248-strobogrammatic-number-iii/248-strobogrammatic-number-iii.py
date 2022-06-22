class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        possible = ['0','1','6','8','9']
        num_of_possible = [0] * 10
        num_of_possible[0] = 1
        mid_possible = [1,2,2,2,2,2,2,2,3,3]
        for i in range(1, 10):
            if str(i) in possible:
                num_of_possible[i] = num_of_possible[i-1] + 1
            else:
                num_of_possible[i] = num_of_possible[i-1]
        mapping = {0:0,1:1,8:8,9:6,6:9}
        dp = [0] * 15
        dp[0] = 0
        dp[1] = 3
        for i in range(2, 15):
            dp[i] = 1
            for j in range(i//2):
                if j == 0:
                    dp[i] = dp[i] * 4
                else:
                    dp[i] = dp[i] * 5
            if i%2 == 1:
                dp[i] = dp[i] * 3
            dp[i] += dp[i-1]
        def check(string):
            if len(string) <= 1:
                return True
            if mapping[int(string[0])] == int(string[-1]):
                return check(string[1:-1])
            else:
                return False
        def count_strob(string, is_leading):
            str_len = len(string)
            if str_len < 1:
                return 0
            if int(string) < 0:
                return 0
            if str_len == 1:
                return mid_possible[int(string[0])]
            count = 0
            #if the first is possible:
            if string[0] in possible and mapping[int(string[0])] <= int(string[-1]):
                nxt = count_strob(string[1:-1], False)
                count += nxt
                count = max(count, 1)
            elif string[0] in possible:
                diff = 0
                if check(string[1:-1]):
                    diff = 1
                nxt = count_strob(string[1:-1], False)
                count += nxt  
                count = max(count, 1) - diff
                
            first_possible = int(string[0]) - 1
            temp = 0
            if is_leading and first_possible > 0:
                temp = (num_of_possible[first_possible] - 1) * 5**(str_len//2 - 1)
                if str_len%2 == 1:
                    temp = temp * 3
            elif not is_leading and first_possible >= 0:
                temp = (num_of_possible[first_possible]) * 5**(str_len//2 - 1)
                if str_len%2 == 1:
                    temp = temp * 3                
            return count + temp

                    
        lower_dp = 0
        lower = str(int(low) - 1)    
        if int(lower) > 0:
            lower_dp = dp[len(lower) - 1]
        return count_strob(high, True) + dp[len(high)-1]- count_strob(lower, True) - lower_dp