class Solution {
    public int minJumps(int[] arr) {
        HashMap<Integer, List<Integer>> valueToIndex = new HashMap<Integer, List<Integer>>();
        int N = arr.length;
        //construct value2index hashmap
        for(int i = 0; i < arr.length; i++){
            valueToIndex.computeIfAbsent(arr[i], x -> new LinkedList<>()).add(i);
        }
        boolean[] visited = new boolean[arr.length];
        Set<Integer> head = new HashSet<>();
        Set<Integer> tail = new HashSet<>();
        head.add(0);
        tail.add(N - 1);
        visited[N-1] = true;
        visited[0] = true;
        int step_count = 0;
        //BFS
        while(!head.isEmpty() && !tail.isEmpty()){
            if(head.size() > tail.size()){
                Set<Integer> temp = head;
                head = tail;
                tail = temp;
            }
            Set<Integer> next = new HashSet<>();
            for(int idx : head){
                if (tail.contains(idx)) return step_count;
                for (int z : valueToIndex.get(arr[idx])){
                    if (tail.contains(z)) return step_count + 1;
                    if (!visited[z]){
                        visited[z] = true;
                        next.add(z);
                    }
                }
                valueToIndex.get(arr[idx]).clear();
                if(tail.contains(idx-1)) return step_count + 1;
                if(tail.contains(idx+1)) return step_count + 1;
                if (idx - 1 >= 0 && !visited[idx-1]){
                    visited[idx-1] = true;
                    next.add(idx-1);
                }
                if (idx + 1 < N && !visited[idx+1]){
                    visited[idx+1] = true;
                    next.add(idx+1);
                }
            }
            
            head = next;
            step_count++;
        }
        return step_count;
    }
}