class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        LinkedList<int[]> directions = new LinkedList<>(Arrays.asList(new int[][]{{0,1},{1,0},{0,-1},{-1,0}}));
        List<Integer> res = new LinkedList<>();
        int nRow = matrix.length, nCol = matrix[0].length;
        int x = 0, y = 0;
        res.add(matrix[0][0]);
        matrix[0][0] = -101;
        for(int i = 0; i < nRow*nCol - 1; i++){
            while(true){
                int[] curDir = directions.peekFirst();
                int newx = x + curDir[0], newy = y + curDir[1];
                if(newx < 0 || newx >= nRow || newy < 0 || newy >= nCol || matrix[newx][newy] == -101){
                    directions.pollFirst();
                    directions.addLast(curDir);
                }else{
                    
                    res.add(matrix[newx][newy]);
                    x = newx;
                    y = newy;
                    matrix[newx][newy] = -101;
                    break;
                }
            }   
        }
        return res;
        
        
    }
}