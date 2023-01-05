class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) return 0;
        
        //sort by x_end
        Arrays.sort(points, (a, b) -> (Integer.compare(a[1], b[1])));
        
        int numArrow = 1;
        int prevEnd = points[0][1];
        for (int[] point : points){
            int curStart = point[0];
            if (prevEnd < curStart){
                numArrow++;
                prevEnd = point[1];
            }
        }
        
        return numArrow;
    
    
    
    }
}