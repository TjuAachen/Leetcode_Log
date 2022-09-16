class Solution {
    public int largestRectangleArea(int[] heights) {
        //leftLargest
        LinkedList<int[]> leftStack = new LinkedList<>();
        int N = heights.length;
        int[] leftSmallest = new int[N];
        int[] rightSmallest = new int[N];
        
        for(int i = 0; i < N; i++){
            int height = heights[i];
            rightSmallest[i] = N;
            //left largest
            while(!leftStack.isEmpty() && leftStack.peekLast()[0] >= height){
                int[] popped = leftStack.pollLast();
                rightSmallest[popped[1]] = i;
                }
                if(leftStack.isEmpty()){
                    leftSmallest[i] = -1;
                }else{
                    leftSmallest[i] = leftStack.peekLast()[1];
                }
            leftStack.addLast(new int[]{height, i});
        }
        int ans = 0;
        for(int j = 0; j < N; j++){
            int curHeight = heights[j];
            int left = leftSmallest[j], right = rightSmallest[j];
          //  System.out.printf("%d %d\n", left, right);
            if(left != j){
                left = left + 1;
            }
            if(right != j){
                right = right - 1;
            }
            ans = Math.max(ans, (right - left + 1) * curHeight);
        }
        return ans;      
    }
}