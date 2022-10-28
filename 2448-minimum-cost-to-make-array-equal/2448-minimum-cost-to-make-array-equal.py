class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        maxVal = 0
        k = 0
        idx2cost = defaultdict(int)
        sortedNums = []
        coef = 0
        for i, num in enumerate(nums):
            idx2cost[i] = cost[i]
            coef -= cost[i]
            sortedNums.append([num, i])
            maxVal += num * cost[i]
        sortedNums.sort()
        curVal = maxVal
        boundary = sortedNums[0][0]
        ans = max(curVal + boundary * coef, 0)
       # print(ans, coef, curVal, boundary)
        for j in range(len(sortedNums) - 1):
            num, i = sortedNums[j]
            curVal = curVal - 2 * idx2cost[i] * num
            coef += 2 * idx2cost[i]
            boundary = sortedNums[j + 1][0]
            curAns = max(curVal + boundary * coef, 0)
            ans = min(ans, curAns)
         #   print(num, i, coef, curAns)
        return ans
        
        