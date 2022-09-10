class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        LinkedList<int[]> intervalsList = new LinkedList<>();
        
        //binary search left, right

        int leftIdx = binarySearch(intervals, newInterval[0]);
        if(leftIdx == -1){
            intervalsList.addLast(newInterval);
        }
        for(int i = 0; i < intervals.length; i++){
            if(i < leftIdx){
                intervalsList.addLast(intervals[i]);
            }else if(i == leftIdx){
                if(intervals[i][1] >= newInterval[0]){
                    intervals[i][1] = Math.max(intervals[i][1],newInterval[1]);
                    intervalsList.addLast(intervals[i]);
                }else{
                    intervalsList.addLast(intervals[i]);
                    intervalsList.addLast(newInterval);
                }
            }else{
                if(intervalsList.peekLast()[1] >= intervals[i][0]){
                    intervalsList.peekLast()[1] = Math.max(intervalsList.peekLast()[1],intervals[i][1]);
                }else{
                    intervalsList.addLast(intervals[i]);
                }
            }
            }
        int[][] res = new int[intervalsList.size()][2];
        for(int j = 0; j < intervalsList.size(); j++){
            res[j][0] = intervalsList.get(j)[0]; res[j][1] = intervalsList.get(j)[1];
            
        }
        return res;
            
            
            
        }
        
        public int binarySearch(int[][] intervals, int val){
        int left = 0, right = intervals.length - 1;
        while(left <= right){
            int mid = left +(right - left) / 2;
            if(intervals[mid][0] >= val){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return right;
        
        
    }
    
    
}