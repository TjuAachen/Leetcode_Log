class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        TreeMap<Integer, Integer> heightNum = new TreeMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0]? a[0] - b[0] : a[2] - b[2]);
        for(int[] building : buildings){
            int in = building[0], out = building[1], height = building[2];
            int[] height_in = new int[]{in, height, 0};
            int[] height_out = new int[]{out, height, 1};
            pq.add(height_in);
            pq.add(height_out);
            
        }
        //enter or exit to update heightNum
        Map<Integer, Integer> posToHeight = new TreeMap<>();
        int maxHeight = 0;
        while(!pq.isEmpty()){
            int[] popped = pq.poll();
            int curHeight = popped[1];
            int curPos = popped[0];
            //if out
            if(popped[2] == 1){
                heightNum.put(curHeight, heightNum.get(curHeight) - 1);
                if (heightNum.get(curHeight) == 0){
                    heightNum.remove(curHeight);
                }
            }else{
                heightNum.computeIfAbsent(curHeight, k -> 0);
                heightNum.put(curHeight, heightNum.get(curHeight) + 1);
            }
            if(heightNum.isEmpty()){
                maxHeight = 0;
                posToHeight.put(curPos, 0);
            }else{
            int curMaxHeight = heightNum.lastKey();
            if(curMaxHeight != maxHeight){
                posToHeight.put(curPos, curMaxHeight);
                maxHeight = curMaxHeight;
            }
            }
        }
        List<List<Integer>> ans = new LinkedList<>();
        for(Map.Entry<Integer, Integer> entry : posToHeight.entrySet()){
            List<Integer> temp_res = new LinkedList<>(Arrays.asList(entry.getKey(), entry.getValue()));
            ans.add(temp_res);
        }
        return ans;
        
        
    }
}