class Solution {
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        // distance used as visited
        HashMap<List<Integer>, Integer> dist = new HashMap<>();
        
        //visited hashmap
        HashSet<List<Integer>> visited = new HashSet<>();
        
        // direction array
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        
        //pq
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[2] - b[2]));
        
        pq.offer(new int[]{start[0], start[1], 0});
        
        int nrow = maze.length, ncol = maze[0].length;
        
        visited.add(Arrays.asList(start[0], start[1]));
        //Dijkstra
        while(!pq.isEmpty()){
            int[] temp_start = pq.poll();
            int x = temp_start[0], y = temp_start[1], temp_dist = temp_start[2];
            if (dist.containsKey(Arrays.asList(x, y))) continue;
            if (x == destination[0] && y == destination[1]) return temp_dist;
            dist.put(Arrays.asList(x, y), temp_dist);
            //traverse
            //System.out.println(y);
            for(int[] direction : directions){
                int temp_x = x, temp_y = y;
                int count = 0;
                while(temp_x + direction[0] < nrow && temp_x + direction[0] >= 0 && temp_y + direction[1] < ncol && temp_y + direction[1] >= 0 && maze[temp_x + direction[0]][temp_y + direction[1]] != 1){
                    temp_x = temp_x + direction[0];
                    temp_y = temp_y + direction[1];                    
                    //visited
                    count++;
                    
                }
         /*       if (visited.contains(Arrays.asList(temp_x, temp_y))){
                        continue;
                    }
                visited.add(Arrays.asList(temp_x, temp_y));*/
                //System.out.printf("%d, %d\n", temp_x, temp_y);
                if (!dist.containsKey(Arrays.asList(temp_x, temp_y))) pq.offer(new int[]{temp_x, temp_y, temp_dist + count});
                
            
            
        }  
    }
        return -1;
}
}