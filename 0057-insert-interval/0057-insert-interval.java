class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // create a new list for the final answer
        List<int[]> resIntervals = new LinkedList<>();
        boolean isPlaced = false;
        
        for (int[] interval : intervals) {
            int left = interval[0], right = interval[1];
            // left non-overlapping intervals add
            if (right < newInterval[0]) {
                resIntervals.add(interval);
            //add right non-overlapping intervals    
            } else if (left > newInterval[1]) {
                if (!isPlaced) {
                    resIntervals.add(newInterval);
                    isPlaced = true;
                }
                resIntervals.add(interval);
            } else {
                newInterval[0] = Math.min(newInterval[0], left);
                newInterval[1] = Math.max(newInterval[1], right);
            }
        }
        
        if (!isPlaced) {
            resIntervals.add(newInterval);
        }
        
        int[][] ans = new int[resIntervals.size()][2];
        int curIdx = 0;
        
        for (int[] interval : resIntervals) {
            ans[curIdx][0] = interval[0];
            ans[curIdx][1] = interval[1];
            curIdx++;
        }
        
        return ans;
    }
        

    
    
}