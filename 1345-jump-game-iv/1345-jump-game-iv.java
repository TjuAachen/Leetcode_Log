class Solution {
    public int minJumps(int[] arr) {
        HashMap<Integer, List<Integer>> valueToIndex = new HashMap<Integer, List<Integer>>();
        
        //construct value2index hashmap
        for(int i = 0; i < arr.length; i++){
            if (! valueToIndex.containsKey(arr[i])){
                ArrayList<Integer> temp = new ArrayList<Integer>();
                temp.add(i);
                valueToIndex.put(arr[i], temp);
            }else{
                valueToIndex.get(arr[i]).add(i);
            }
        }
        boolean[] visited = new boolean[arr.length];
        Deque<Integer> deque = new LinkedList<Integer>();
        deque.offer(0);
        visited[0] = true;
        int step_count = 0;
        //BFS
        while(!deque.isEmpty()){
            int size = deque.size();
            for(int i = 0; i < size; i++){
                int index = deque.poll();
                //add i-1, i+1
                if (index == arr.length - 1) return step_count;
                List<Integer> neighbors = valueToIndex.get(arr[index]);
                neighbors.add(index-1);
                neighbors.add(index+1);
                for(int idx : neighbors){
                    if (idx < arr.length && idx >= 0 && !visited[idx]){
                    //    if (idx == arr.length - 1) return step_count;
                        deque.offer(idx);
                        visited[idx] = true;
                    }
                }
                valueToIndex.get(arr[index]).clear();
                
            }
            step_count++;
        }
        return step_count;
    }
}