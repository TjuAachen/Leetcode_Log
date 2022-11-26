from sortedcontainers import SortedDict
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        self.endTimeMaxProfit = SortedDict()
        self.endTimeStartTime = SortedDict()
        
        n = len(startTime)
        
        for i in range(n):
            curStart = startTime[i]
            curEnd = endTime[i]
            curProfit = profit[i]
            
            if curEnd not in self.endTimeMaxProfit:
                self.endTimeMaxProfit[curEnd] = []
                self.endTimeStartTime[curEnd] = []
                self.endTimeMaxProfit[curEnd].append(curProfit)
                self.endTimeStartTime[curEnd].append(curStart)
            else:
                self.endTimeMaxProfit[curEnd].append(curProfit)
                self.endTimeStartTime[curEnd].append(curStart)                
        
        self.minEndTime = self.endTimeMaxProfit.peekitem(0)[0]
        self.maxEndTime = self.endTimeMaxProfit.peekitem(-1)[0]
        
        length = len(self.endTimeMaxProfit)
        

        return self.maxProfit(length - 1, self.maxEndTime, dict())
        
    def maxProfit(self, Idx, curEndTime, memo):
        if curEndTime < self.minEndTime:
            return 0
        
        if Idx < 0:
            return 0
        
        if curEndTime in memo:
            return memo[curEndTime]
        
        res = 0

        #select
        for i, profit in enumerate(self.endTimeMaxProfit[curEndTime]):

            curStartTime = self.endTimeStartTime[curEndTime][i]
            prevEndTimeIdx = self.endTimeMaxProfit.bisect(curStartTime) - 1
            
            
            prevEndTime = self.endTimeMaxProfit.peekitem(prevEndTimeIdx)[0]
            
            res = max(res, self.maxProfit(prevEndTimeIdx, prevEndTime, memo) + profit)
        
        #not select
        prevEndTime = self.endTimeMaxProfit.peekitem(Idx - 1)[0]
        
        res = max(res, self.maxProfit(Idx - 1, prevEndTime, memo))
        
        memo[curEndTime] = res
        
        return res
        
        
        
            
        
        
        
        
        