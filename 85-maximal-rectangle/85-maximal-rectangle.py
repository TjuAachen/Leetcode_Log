class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        nrow, ncol = len(matrix), len(matrix[0])
        def maxArea(heights):
            stack = [-1]
            res = 0
            for i in range(ncol):
               # top = heights[stack[-1]]
                while(stack[-1] != -1 and heights[stack[-1]] > heights[i] ):
                    popped = stack.pop()
                    width = i - stack[-1] - 1
                    height = heights[popped]
                    res = max(res,width*height)
                stack.append(i)
            while(stack[-1] != -1):
                popped = stack.pop()
                width = ncol - stack[-1] - 1
                height = heights[popped]
                res = max(res,width*height)   
            return res
        final = 0
        heights = []
        for i in range(nrow):
            for j in range(ncol):
                if len(heights) < ncol:
                    if matrix[i][j] == "1":
                        heights.append(1)
                    else:
                        heights.append(0)
                elif matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
           # print(heights)
            final = max(maxArea(heights),final)
        return final
            
                
                    
                        
        
                            
                        
                    
        