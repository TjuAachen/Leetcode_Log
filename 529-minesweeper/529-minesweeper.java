class Solution {
    private int revealedCount = 0;
    private boolean isHit = false;
    private int[][] neighbors = new int[][]{{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
    public char[][] updateBoard(char[][] board, int[] click) {
        int nrow = board.length, ncol = board[0].length;
        LinkedList<Pair> queue = new LinkedList<>();
        int MineNum = this.countMine(board, click[0], click[1]);
        char cur_char = board[click[0]][click[1]];
        HashSet<Pair> visited = new HashSet<>();
        if(cur_char == 'M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }
        if(MineNum > 0){
            board[click[0]][click[1]] = Integer.toString(MineNum).charAt(0);
            return board;
        }
        
        queue.addLast(new Pair(click[0], click[1]));
        
        while(!queue.isEmpty()){
            //termination
            int size = queue.size();
            for(int i = 0; i < size; i++){
                Pair popped = queue.pollFirst();
                int x = (int) popped.getKey(), y =(int) popped.getValue();
                cur_char = board[x][y];
                board[x][y] = 'B';

                //traverse from adjacent
                for(int[] direction : neighbors){
                    int newx = x + direction[0], newy = y + direction[1];
                    if(newx < nrow && newx >= 0 && newy < ncol && newy >= 0 && board[newx][newy] == 'E' && !visited.contains(new Pair(newx, newy))){
                        visited.add(new Pair(newx, newy));
                        int curMineNum = this.countMine(board, newx, newy);
                        if(curMineNum == 0){
                            queue.addLast(new Pair(newx, newy));
                        }else if (curMineNum > 0){
                            board[newx][newy] = Integer.toString(curMineNum).charAt(0);
                            
                        }
                    }
            
                }
            
            }
        
        }
       return board; 
    }
    public int countMine(char[][] board, int row, int col){

        int nrow = board.length, ncol = board[0].length;
        int ans = 0;
        for(int[] neighbor : neighbors){
            int newx = row + neighbor[0], newy = col + neighbor[1];
            if(newx < nrow && newx >= 0 && newy < ncol && newy >= 0 && (board[newx][newy] == 'M' || board[newx][newy] == 'X'))
                ans++;
        }
        return ans;
    }
}