class Solution {
    public int maxArea(int[] height) {
        int N = height.length;
        int left = 0, right = N - 1;
        
        
        
        int res = 0;
        while(left < right){
            res = Math.max(res,Math.min(height[left], height[right]) * (right - left));
            int cur_min = Math.min(height[left], height[right]);
            if(cur_min == height[left]){
                int temp = left;
                while(temp < right && height[temp] <= height[left]){
                    temp++;
                }
                left = temp;
            }else if (cur_min == height[right]){
                int temp = right;
                while(temp > left && height[temp] <= height[right]){
                    temp--;
                }
                right = temp;                
            }
        }
        return res;
        
        
    }
}