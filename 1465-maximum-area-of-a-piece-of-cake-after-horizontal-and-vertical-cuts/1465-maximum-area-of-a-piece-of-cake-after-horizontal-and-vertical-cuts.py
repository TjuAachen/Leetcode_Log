class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        horizontalCuts.insert(0, 0) 
        horizontalCuts.sort()
        verticalCuts.append(w)
        verticalCuts.insert(0, 0)
        verticalCuts.sort()
        max_width = 0
        max_length = 0
        for i, horizontalCut in enumerate(horizontalCuts):
            if i > 0:
                max_width = max(max_width,horizontalCut - horizontalCuts[i-1])
        for i, verticalCut in enumerate(verticalCuts):
            if i > 0:
                max_length = max(max_length,verticalCut - verticalCuts[i-1])
        return ( max_width * max_length)%(10**9+7)