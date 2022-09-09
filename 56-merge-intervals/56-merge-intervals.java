class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals , (o1,o2)-> o1[0]!=o2[0]?o1[0]-o2[0]:o1[1]-o2[1]);
        LinkedList<int[]> res = new LinkedList<>();
        
        for(int i = 0; i < intervals.length; i++){
            int[] curInterval = intervals[i];
            if(res.isEmpty())
            {
                res.add(intervals[i]);
            }else{
                int[] tail = res.peekLast();
                if(tail[1] >= curInterval[0]){
                    tail[1] = Math.max(curInterval[1], tail[1]);
                }else{
                    res.add(intervals[i]);
                }
                
            }   
        }
        
        int[][] ans = new int[res.size()][2];
        int j = 0;
        for(int[] temp : res){
            ans[j][0] = temp[0];
            ans[j++][1] = temp[1];  
        }
        return ans;
        
        
        
    }
}