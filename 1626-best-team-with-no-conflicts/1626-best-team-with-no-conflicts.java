class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        int n = scores.length;
        int[][] combinedArray = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            combinedArray[i][0] = scores[i];
            combinedArray[i][1] = ages[i];
        }
        
        Arrays.sort(combinedArray , (o1,o2)-> o1[1]!=o2[1]?o1[1]-o2[1]:o1[0]-o2[0]);
  
        //starting from i, the maxValues
        int[] maxValues = new int[n]; 
        //initialize
        maxValues[n - 1] = combinedArray[n - 1][0];
        int ans = maxValues[n - 1];
        
        for (int left = n - 2; left >= 0; left--) {
            int prevAge = combinedArray[left][1];
            int prevScore = combinedArray[left][0];
            maxValues[left] = prevScore;
            for (int right = left + 1; right < n; right++) {
                int curAge = combinedArray[right][1];
                int curScore = combinedArray[right][0];
                
                if (curAge > prevAge && prevScore > curScore)
                    continue;
                maxValues[left] = Math.max(maxValues[left], maxValues[right] + prevScore);
            }
            ans = Math.max(ans, maxValues[left]);
           // System.out.printf("%d %d %d\n", prevScore, left, ans);
        }
        
        return ans;
        

    }
}