class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        LinkedList<int[]> intervalsList = new LinkedList<>();
        
   //     Arrays.sort(intervals);
        //add intervals starting before newInterval
        int idx = 0;
        while(idx < intervals.length && intervals[idx][1] < newInterval[0]){
            intervalsList.addLast(intervals[idx++]);
        }
        
        //merge overlapping intervals
        while(idx < intervals.length && intervals[idx][0] <= newInterval[1]){
            newInterval[0] = Math.min(newInterval[0], intervals[idx][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[idx][1]);
            idx++;
        }
        intervalsList.addLast(newInterval);
        
        //add later intervals
        while(idx < intervals.length){
            intervalsList.addLast(intervals[idx++]);
        }

            
            
            
    return intervalsList.toArray(new int[0][0]);    
    }
        

    
    
}