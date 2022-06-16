class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        #ax1<= x1 <= ax2
        #ay1<= y1 <= ay2
        
        #bx1<= x2 <= bx2
        #by1<= y2 <= by2
        newX1, newY1 = max(ax1,bx1), max(ay1,by1)
        newX2, newY2 = min(ax2,bx2), min(ay2,by2)
        
        if (newX2 - newX1) < 0 or (newY2 - newY1) < 0:
            common_area = 0
        else:
            common_area = (newX2 - newX1) * (newY2 - newY1)
        area1 = (ax2-ax1) * (ay2-ay1)
        area2 =(bx2-bx1) * (by2-by1)
        return area1 + area2 - max(common_area, 0)