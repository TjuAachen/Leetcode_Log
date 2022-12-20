class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        
        
        return dfs(0, rooms, new HashSet<Integer>());
        
    }
    
    public boolean dfs(int room, List<List<Integer>> rooms, Set<Integer> visited){
        
        int numRooms = rooms.size();
        
        visited.add(room);
        if (visited.size() == numRooms)
            return true;
        for (int nxtRoom : rooms.get(room)){
            if (visited.contains(nxtRoom))
                continue;
            if (dfs(nxtRoom, rooms, visited))
                return true;
        }
        return (visited.size() == numRooms);

    }
    
}