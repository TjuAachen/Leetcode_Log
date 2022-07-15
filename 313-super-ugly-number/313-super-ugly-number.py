from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        factors = []
        uglyNums = [1]
        heapify(factors)
        num_primes = len(primes)
        for prime in primes:
            heappush(factors,[prime*uglyNums[0], prime, 0])

        while(len(uglyNums) < n):
            cur_maximum, prime, idx = heappop(factors)
            if cur_maximum != uglyNums[-1]:
                uglyNums.append(cur_maximum)
            heappush(factors, [prime*uglyNums[idx+1], prime, idx+1])
            
        return uglyNums[-1]
            
        
        
        