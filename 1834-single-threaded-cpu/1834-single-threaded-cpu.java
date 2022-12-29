class Solution {
    public int[][] IndexAndSort(int[][] tasks){
        int n = tasks.length;
        int i = 0;
        int[][] taskIndex = new int[n][3];
        for (int[] task : tasks){
            taskIndex[i][0] = i;
            taskIndex[i][1] = task[0];
            taskIndex[i][2] = task[1];
            i++;
        }
        Arrays.sort(taskIndex, (a, b) -> a[1] != b[1] ? a[1] - b[1] : a[2] - b[2]);
        
        return taskIndex;
    }
    
    
    public int[] getOrder(int[][] tasks) {
        //int [index, processing time]
        PriorityQueue<int[]> waitingTasks = new PriorityQueue<>((a, b) -> (a[1] != b[1]?a[1] - b[1] : a[0] - b[0]));
        int curTime = 0;
        
        int n = tasks.length;
        int[][] indexedTasks = IndexAndSort(tasks);
        int[] ans = new int[n];
        int curOrder = 0;
        int i = 0;
        
        while(i < n || !waitingTasks.isEmpty()){
            while(!waitingTasks.isEmpty()){
                int[] completedTask = waitingTasks.poll();
                ans[curOrder++] = completedTask[0];
                curTime += completedTask[1];
                while(i < n && indexedTasks[i][1] <= curTime){
                    waitingTasks.add(new int[]{indexedTasks[i][0], indexedTasks[i][2]});
                    i++;
                }
            }
            
            if (i == n){
                return ans;
            }
            curTime = Math.max(indexedTasks[i][1], curTime);
            while (i < n && indexedTasks[i][1] == curTime){
                waitingTasks.add(new int[]{indexedTasks[i][0], indexedTasks[i][2]});
                curTime = Math.max(indexedTasks[i][1], curTime);
                i++;                
            }
        }
        
        return ans;
        
        
        
        
    }
}