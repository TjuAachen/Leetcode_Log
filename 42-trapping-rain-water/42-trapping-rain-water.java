class Solution {
    public int trap(int[] height) {
        int N = height.length;
        int left = 0, right = N - 1;
        int leftMax = 0, rightMax = 0;
        int ans = 0;
        while(left < right){
            if(height[left] < height[right]){
                //说明left一定能储水
                if(height[left] >= leftMax){
                    leftMax = height[left];
                }else{
                    ans += (leftMax - height[left]);
                }
                left++;
            }else{
                //说明right一定能储水
                if(height[right] >= rightMax){
                    rightMax = height[right];
                }else{
                    ans += (rightMax - height[right]);
                }
                right--;
            }
        }
        return ans;

    }

}