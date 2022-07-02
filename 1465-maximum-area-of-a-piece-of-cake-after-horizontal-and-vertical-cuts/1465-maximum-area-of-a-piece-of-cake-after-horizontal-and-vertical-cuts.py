class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        horizontalCuts.insert(0, 0) 
        horizontalCuts.sort()
        verticalCuts.append(w)
        verticalCuts.insert(0, 0)
        verticalCuts.sort()
        width = []
        length = []
        for i, horizontalCut in enumerate(horizontalCuts):
            if i > 0:
                width.append(horizontalCut - horizontalCuts[i-1])
        for i, verticalCut in enumerate(verticalCuts):
            if i > 0:
                length.append(verticalCut - verticalCuts[i-1])
        return (max(width) * max(length))%(10**9+7)