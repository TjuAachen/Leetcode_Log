class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        time = []
        for grow, plant in zip(growTime, plantTime):
            time.append([grow, plant])
        time.sort(key = lambda x: -x[0])
        
        ans = 0
        maxNum = -1
        for i, val in enumerate(time):
            grow, plant = val
            if i == 0:
                ans += grow +plant
            else:
                ans += grow + plant - time[i - 1][0]
            maxNum = max(maxNum, ans)
        return maxNum
        