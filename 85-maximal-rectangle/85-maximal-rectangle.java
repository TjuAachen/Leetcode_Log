class Solution {
    int nrow;
    int ncol;
    public int maximalRectangle(char[][] matrix) {
        nrow = matrix.length; ncol = matrix[0].length;
        int[][] numOfOne = new int[nrow][ncol];
        countOne(numOfOne, matrix);
        int ans = 0;
        for(int[] array : numOfOne){
            ans = Math.max(ans, findLargestRec(array));
        }
        return ans;
        
        
        
    }
    public void countOne(int[][] numOfOne, char[][] matrix){
        for(int row = 0; row < nrow; row++)
            for(int col = 0; col < ncol; col++){
                char curChar = matrix[row][col];
                if(curChar == '1'){
                    numOfOne[row][col] += 1;
                }
                if(row > 0 && matrix[row-1][col] == '1' && matrix[row][col] == '1'){
                    numOfOne[row][col] += numOfOne[row - 1][col];
                }
            }
    }
    
    public int findLargestRec(int[] heights){
     //   System.out.printf("%d %d\n", heights[0], heights[1]);
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
