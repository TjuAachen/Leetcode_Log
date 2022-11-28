class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)
        
        prevNodes = defaultdict(list)
        
        numOfTwo = defaultdict(int)
        numOfThree = defaultdict(int)
        
        
        
        diff = [set() for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                curDiff = nums[j] - nums[i]
                key = tuple([j, curDiff])
                prevNodes[key].append(i)
                numOfTwo[key] += 1
                
                diff[j].add(curDiff)
                

        #length of 3 or above
        ans = 0
         
        for i in range(2, n):
            #choose
            #must know the possible diff
            for curDiff in diff[i]:
                key = tuple([i, curDiff])
                for prev in prevNodes[key]:
                    prevKey = tuple([prev, curDiff])
                    numOfThree[key] += numOfTwo[prevKey] + numOfThree[prevKey]
            

                ans += numOfThree[key] 
        return ans
                
            
            
         
        
        
        
        #choose
    #    numOfThree[curEnd][diff] = numOfTwo[curEnd - diff][diff] + numOfThree[curEnd - diff][diff]
        #not choose
   #     numOfThree[curEnd][diff] += numOfThree[prev][diff]
        
        
        
        
        
            
        
        
        