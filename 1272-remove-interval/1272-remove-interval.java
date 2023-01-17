class Solution {
    public List<List<Integer>> removeInterval(int[][] intervals, int[] toBeRemoved) {
        List<List<Integer>> resIntervals = new LinkedList<>();
        
        for (int[] interval : intervals) {
            //left non-overlapping
            if (interval[1] <= toBeRemoved[0]) 
                resIntervals.add(Arrays.asList(interval[0], interval[1]));
            else if (interval[0] >= toBeRemoved[1]) 
                resIntervals.add(Arrays.asList(interval[0], interval[1]));
            else{
                if (interval[0] < toBeRemoved[0] && interval[1] > toBeRemoved[1]) {
                    resIntervals.add(Arrays.asList(interval[0], toBeRemoved[0]));
                    resIntervals.add(Arrays.asList(toBeRemoved[1], interval[1]));
                } else if (interval[0] < toBeRemoved[0]) {
                    interval[1] = toBeRemoved[0];
                    resIntervals.add(Arrays.asList(interval[0], interval[1]));
                } else if (interval[1] > toBeRemoved[1]) {
                    interval[0] = toBeRemoved[1];
                    resIntervals.add(Arrays.asList(interval[0], interval[1]));
                }
            }
        }
        
        return resIntervals;
        
        
    }
}