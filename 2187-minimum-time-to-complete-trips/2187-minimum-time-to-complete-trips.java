class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        long res = 0;
        
        long left = 0;
        long right = 100000000000000l;
        
        while (left + 1 < right) {
            long mid = left + (right - left) / 2;
            long curTripNum = numOfTrips(time, mid);
            
            if (curTripNum >= totalTrips) {
                right = mid;
            }else {
                left = mid;
            }
        }
        if (numOfTrips(time, left) >= totalTrips)
            return left;
        return right;

    }
    
    public long numOfTrips(int[] time, long curTime) {
        long res = 0;
        for (int val : time) {
            res += curTime / val;
        }
        
        return res;
    }
}