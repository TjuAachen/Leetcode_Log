class Solution {
    public boolean canReach(int[] arr, int start) {
        boolean[] visited = new boolean[arr.length];
        Deque<Integer> deque = new LinkedList<Integer>();
        deque.push(start);
        visited[start] = true;
        while(!deque.isEmpty()){
            int size = deque.size();
            for(int i = 0; i < size; i++){
                int temp = deque.poll();
                if (temp + arr[temp] < arr.length && !visited[temp + arr[temp]]){
                    deque.push(temp + arr[temp]);
                    visited[temp + arr[temp]] = true;
                }
                if (temp - arr[temp] >= 0 && !visited[temp - arr[temp]]){
                    deque.push(temp - arr[temp]);
                    visited[temp - arr[temp]] = true;
                }
                if (arr[temp] == 0){
                    return true;
                }
            }
        }
        return false;
        
    }
}