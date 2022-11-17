class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        
        int left = Math.max(ax1, bx1);
        int right = Math.min(ax2, bx2);
        
        int up = Math.min(ay2, by2);
        int down = Math.max(ay1, by1);
        
        int areaSum = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1);
        
        if((up - down)<= 0 || (right - left) <= 0){
            return areaSum;
        }
        
        int area = (up - down) * (right - left);
        
        return areaSum - area;
    }
}