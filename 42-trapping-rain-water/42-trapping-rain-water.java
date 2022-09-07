class Solution {
    public int trap(int[] height) {
        int N = height.length;
        int[] leftMost = new int[N];
        int[] rightMost = new int[N];
        int curLeftMost = -1, curRightMost = -1;
        for(int k = 0; k < N; k++){
            if(height[k] >= curLeftMost) {
                leftMost[k] = -1;
                curLeftMost = height[k];
            }else{
                leftMost[k] = curLeftMost;
            }
        }
        for(int m = N - 1; m >= 0; m--){ 
            if(height[m] >= curRightMost) {
                rightMost[m] = -1;
                curRightMost = height[m];
            }else{
                rightMost[m] = curRightMost;
            }
        }
        
        int ans = 0;
        for(int j = 0; j < N; j++){
            if(leftMost[j] == -1 || rightMost[j] == -1)continue;
            int maxHeight = Math.min(leftMost[j], rightMost[j]);
            ans += maxHeight - height[j];
        }
        return ans;
    }

}