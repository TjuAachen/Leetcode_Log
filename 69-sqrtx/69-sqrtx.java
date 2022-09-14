class Solution {
    public int mySqrt(int x) {
        int left = 0, right = x;
        while(left <= right){
            int mid = left + (right - left) / 2;
            int val;
            if(mid != 0 && mid > (Integer.MAX_VALUE)/mid){
                val = Integer.MAX_VALUE;
            }else{
                val = mid * mid;
            }
            if(val == x && x != Integer.MAX_VALUE)return mid;
            if(val < x){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return right;
    }
}