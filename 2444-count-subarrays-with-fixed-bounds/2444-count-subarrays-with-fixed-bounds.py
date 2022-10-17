class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
		# kmin: number of subarrays ending at last pos that contains minK
		# kmax: number of subarrays ending at last pos that contains maxK
		# start: pos of previous invalid number (namely > maxK or < minK)
        kmin, kmax, start = 0, 0, -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                kmin, kmax, start = 0, 0, i
            else:
                if num == minK:
                    kmin = i - start
                if num == maxK:
                    kmax = i - start            
                ans += min(kmin, kmax)
        return ans
            
                
                
        
                    
                

        
        
        
        
        
        
        