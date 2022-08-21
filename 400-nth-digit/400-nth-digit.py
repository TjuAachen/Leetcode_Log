class Solution:
    def findNthDigit(self, n: int) -> int:
        cur = 9
        i = 1
        count = 0
        while(count + cur * i< n):
            count += cur*i
            i += 1
            cur = cur*10
        target_num = str(10**(i-1) + (n - count) // i)
        remaining = (n - count) % i
        print(target_num, remaining, count, i)
        if remaining - 1 >= 0:
            return int(target_num[remaining - 1])
        return int(str(10**(i-1) + (n - count) // i - 1)[-1])
        