class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        Set<Pair> visited = new HashSet<>();
        
        int nRow = maze.length;
        int nCol = maze[0].length;
        
        LinkedList<int[]> queue = new LinkedList<>();
        
        Pair key = new Pair(entrance[0], entrance[1]);
        visited.add(key);
        queue.addLast(new int[]{entrance[0], entrance[1], 0});
        
        LinkedList<int[]> dirs = new LinkedList<>(Arrays.asList(new int[]{1,0}, new int[]{-1,0}, new int[]{0,1}, new int[]{0,-1}));
        
        while(!queue.isEmpty()){
            
            int size = queue.size();
            
            for(int i = 0; i < size; i++){
                int[] curCell = queue.pollFirst();
                
                for(int[] dir : dirs){
                    int newX = curCell[0] + dir[0];
                    int newY = curCell[1] + dir[1];
                    Pair newKey = new Pair(newX, newY);
                    
                    if(!visited.contains(newKey) && newX >= 0 && newX < nRow && newY >= 0 && newY < nCol && maze[newX][newY] != '+'){
                        visited.add(newKey);
                        
                        if(newX == nRow - 1 || newX == 0 || newY == 0 || newY == nCol - 1)
                            return curCell[2] + 1;
                        
                        queue.addLast(new int[]{newX, newY, curCell[2] + 1});
                        
                    }
                }
            }
        }
        
        return -1;
        
    }
}