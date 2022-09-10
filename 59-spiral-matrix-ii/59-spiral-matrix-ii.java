class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int[][] directions = {{0,1},{1,0},{0,-1},{-1,0}};
        int x = 0, y = 0;
        res[x][y] = 1;
        int j = 0;
        for(int i = 2; i < n*n + 1; i++){
            while(true){
            int newx = directions[j%4][0] + x, newy = directions[j%4][1] + y;
            if(newx < n && newx >= 0 && newy < n && newy >= 0 && res[newx][newy] == 0){
                res[newx][newy] = i;
                x = newx;
                y = newy;
                break;
            }else{
                j++;
            }
        }
        
        }
        return res;
        
        
    }
}