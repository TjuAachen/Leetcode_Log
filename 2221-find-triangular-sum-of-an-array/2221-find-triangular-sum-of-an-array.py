class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        prevNums = nums
        while(len(prevNums) > 1):
            curNums = [0] * (len(prevNums) - 1)
            for i in range(len(curNums)):
                curNums[i] = (prevNums[i] + prevNums[i+1])%10
            prevNums = curNums
        return prevNums[0]
                
        
        