class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 0;
        
        for (int pile : piles) {
            right = Math.max(right, pile);
        }
        
        // binary search
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            
            if (check(piles, mid, h)) {
                right = mid;
            }else {
                left = mid;
            }
        }
        if (check(piles, left, h))
            return (int) left;
        return (int) right;
        
        
        
        
    }
    
    public boolean check(int[] piles, int mid, int h) {
        int needTime = 0;
        int curNum = 0;
        int n = piles.length;
        int i = 0;
        //copy
        
        while (i < n) {
            int curPile = piles[i];
            needTime += curPile / mid + (curPile % mid == 0 ? 0 : 1);
            i++;
        }

        return needTime <= h;
    }
}