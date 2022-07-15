from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        maximum_factor = n // len(primes)
        uglyNums = [1]
        heapify(uglyNums)
        num_primes = len(primes)
        pointers = [0] * num_primes
        while(len(uglyNums) < n):
            candidates = [uglyNums[pointers[i]]*primes[i] for i in range(num_primes)]
            cur_maximum = min(candidates)
            uglyNums.append(cur_maximum)
            for i in range(num_primes):
                while(primes[i] * uglyNums[pointers[i]] <= cur_maximum):
                    pointers[i] += 1
        return uglyNums[-1]
            
        
        
        