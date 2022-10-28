class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        maxRes = 0
        for xShift in range(n):
            for yShift in range(n):
                maxRes = max(maxRes, self.shiftAndCount(xShift, yShift, img1, img2))
                maxRes = max(maxRes, self.shiftAndCount(xShift, yShift, img2, img1))
        return maxRes
        
        
        
    def shiftAndCount(self, xShift, yShift, img1, img2):
        n = len(img1)
        leftCount, rightCount = 0, 0
        for row1, row2 in enumerate(range(yShift, n)):
            for col1, col2 in enumerate(range(xShift, n)):
                if img1[row2][col2] == 1 and img1[row2][col2] == img2[row1][col1]:
                    leftCount += 1
                if img1[row2][col1] == 1 and img1[row2][col1] == img2[row1][col2]:
                    rightCount += 1
        return max(leftCount, rightCount)
        