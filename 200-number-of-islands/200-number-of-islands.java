class Solution {
    public int numIslands(char[][] grid) {
        //dfs
        int count = 0;
        int nrow = grid.length, ncol = grid[0].length;
        for(int row = 0; row < nrow; row++)
            for(int col = 0; col < ncol; col++){
                if(grid[row][col] == '1'){
                    this.findAllNeighbor(row, col, grid);
                    count++;
                }
            }
        return count;
    }
    public void findAllNeighbor(int row, int col, char[][] grid){
        int nrow = grid.length, ncol = grid[0].length;
        //direction
        int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
        grid[row][col] = '0';
        //traverse all the choices and cover any islands
        for(int i = 0; i < 4; i++){
            int[] direction = directions[i];
            int dx = direction[0], dy = direction[1];
            int newx = row + dx, newy = col + dy;
            if( 0 <= newy && newy < ncol && 0 <= newx && newx < nrow && grid[newx][newy] == '1'){
                grid[newx][newy] = '0';
                this.findAllNeighbor(newx, newy, grid);
                
            }
        }
        
    }
}