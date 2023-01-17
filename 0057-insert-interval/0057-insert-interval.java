class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // create a new list for the final answer
        List<int[]> resIntervals = new LinkedList<>();
        int n = intervals.length;
        
        int leftBound = findBoundIdx(newInterval, intervals, true);
        int rightBound = findBoundIdx(newInterval, intervals, false);
      //  System.out.printf("%d %d\n", leftBound, rightBound);
        //deal with left non-overlapping intervals
        for (int idx = 0; idx <= leftBound; idx++) {
            resIntervals.add(intervals[idx]);
        }
        //deal with overlapping intervals
        for (int idx = leftBound + 1; idx < rightBound; idx++) {
            newInterval[0] = Math.min(newInterval[0], intervals[idx][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[idx][1]);
        }
        resIntervals.add(newInterval);
        
        //deal with the right non-overlapping intervals
        for (int idx = rightBound; idx < n; idx++) {
            resIntervals.add(intervals[idx]);
        }
        
        int[][] ans = new int[resIntervals.size()][2];
        int idx = 0;
        
        for (int[] resInterval : resIntervals) {
            ans[idx][0] = resInterval[0];
            ans[idx][1] = resInterval[1];
            idx++;
        }
        
        return ans;
        
        
        
    }
    
    public int findBoundIdx(int[] newInterval, int[][] intervals, boolean isFindingLeft) {
        int n = intervals.length;
        int left = 0, right = n - 1;
        int idx = 1;
        if (n == 0) {
            if (isFindingLeft)
                return -1;
            return 0;
        }
        
  
        if (!isFindingLeft) {
            idx = 0;
        }
        int newIdx = 1 - idx;
        
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (intervals[mid][idx] < newInterval[newIdx]) {
                left = mid;
            }else if (intervals[mid][idx] > newInterval[newIdx]){
                right = mid;
            }else if (isFindingLeft) {
                right = mid;
            }else {
                left = mid;
            }
        }
        if (isFindingLeft) {
            if (intervals[right][idx] < newInterval[newIdx])
                return right;
            if (intervals[left][idx] < newInterval[newIdx])
                return left;
            return -1;
        }
        if (intervals[left][idx] > newInterval[newIdx])
            return left;
        if (intervals[right][idx] > newInterval[newIdx])
            return right;
        return n;       

    }
 
}