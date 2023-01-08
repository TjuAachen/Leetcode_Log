class Solution {
    public int maxPoints(int[][] points) {
        int pointNum = points.length;
        int[] ans = new int[1];
        Map<Pair, Integer> lineNum = new HashMap<Pair, Integer>();
        
        for (int left = 0; left < pointNum; left++)
            for (int right = left + 1; right < pointNum; right++){
                int[] point1 = points[left], point2 = points[right];
                addIntoMap(point1, point2, lineNum, ans);
            }
        
        for (int n = 1; n <= pointNum; n++){
            if (n * (n - 1) == 2 * ans[0])
                return n;
        }
        return 0;
    }
    
    public void addIntoMap(int[] point1, int[] point2, Map<Pair, Integer> lineNum, int[] ans) {
        if (point1[0] == point2[0] && point1[1] == point2[1]) {
            return;
        }
        Pair key = new Pair<>(0, 0);
        if (point1[0] == point2[0]) {
            key = new Pair<>(Integer.MAX_VALUE, (double) point1[0]);
        } else {
            double k = (double) (point2[1] - point1[1]) / (point2[0] - point1[0]);
            if (Math.abs(k) == 0.0){
                k = 0.0;
            }
            double b = (double) (point1[1] * point2[0]  - point1[0] * point2[1]) / (point2[0] - point1[0]);
            
            if (Math.abs(b) == 0)
                b = 0.0;
            
            key = new Pair<>(k, b);
        }
        lineNum.computeIfAbsent(key, k -> 0);
        lineNum.put(key, lineNum.get(key) + 1);
        ans[0] = Math.max(ans[0], lineNum.get(key));
        
    }
}