class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack =[-1]
        res = 0
        n = len(heights)
        for i in range(n):
            while(stack[-1] != -1):
                top = heights[stack[-1]]
                if heights[i] < top:
                    popped = stack.pop()
                    height = heights[popped]
                    width = i - stack[-1]-1
                    res = max(res, height*width)
                else:
                    break
            stack.append(i)
                 #   height = 
        while(stack[-1] != -1):
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            res = max(res, height*width)
        return res
        
        