class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        //@input : 2d int array
        //@output : cur position's height
        //@edge case : empty array
        //@breaking down problem:
        //0. preprocess each input by adding one entry position + positive height, adding one entry position + negative height
        //1.for processed input, if height is positive, add height into the treeSet; if height is negative, remove height from the treeset.
        //after each input or removal, then set the maxValue from the curHeight to the position.
       PriorityQueue<int[]> sortedInput =  new PriorityQueue<>((a, b) -> a[0] != b[0]? a[0] - b[0] : b[1] - a[1]);
        buildInput(buildings, sortedInput);
        
        TreeMap<Integer, Integer> curHeights = new TreeMap<>();
        
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        while(!sortedInput.isEmpty()){
            int[] input = sortedInput.poll();
            int curPosition = input[0];
            //leave 
          //  int maxKey = curHeights.lastEntry().getKey();
            if(input[1] < 0){
                if(curHeights.get(-input[1]) == 1){
                    curHeights.remove(-input[1]);
                }else{
                    curHeights.put(-input[1], curHeights.get(-input[1]) - 1);
                }
            
            //enter
            }else{
                curHeights.computeIfAbsent(input[1], k -> 0);
                curHeights.put(input[1], curHeights.get(input[1]) + 1);
                
            }
            int curMaxHeight = 0;
            if(!curHeights.isEmpty()){
                curMaxHeight = curHeights.lastKey();
            }
            List<Integer> temp = new LinkedList<>(Arrays.asList(curPosition, curMaxHeight));
            if(res.isEmpty() || res.get(res.size() - 1).get(1) != curMaxHeight){
                res.add(temp);
            }
            
        }
        return res;
        
        
        
        
        
    }
    public void buildInput(int[][] buildings, PriorityQueue<int[]> sortedInput){
        
        for(int[] building : buildings){
            int entryPosition = building[0];
            int leavingPosition = building[1];
            int curHeight = building[2];
            sortedInput.offer(new int[]{entryPosition, curHeight});
            sortedInput.offer(new int[]{leavingPosition, -curHeight});
            
        }
    }
    
    
    
    
    
}