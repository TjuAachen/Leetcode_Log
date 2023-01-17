class Solution {
    public int minFlipsMonoIncr(String s) {
        int strLen = s.length();
        int ans = 0;
        int[] prefixOne = new int[strLen];
        int[] prefixZero = new int[strLen];
        int totalZero = 0;
        ans = Integer.MAX_VALUE;
        
        if (s.charAt(0) == '0'){
            prefixZero[0] = 1;
            totalZero += 1;
        }else
            prefixOne[0] = 1;
        
        for (int idx = 1; idx < strLen; idx++) {
            char curChar = s.charAt(idx);
            if (curChar == '0') {
                prefixZero[idx] = prefixZero[idx - 1] + 1;
                prefixOne[idx] = prefixOne[idx - 1];
                totalZero += 1;
            }else {
                prefixOne[idx] = prefixOne[idx - 1] + 1;
                prefixZero[idx] = prefixZero[idx - 1];
                
            }
        }
        
        for (int idx = 0; idx < strLen; idx++) {
            int curAns = prefixOne[idx] + (totalZero - prefixZero[idx]);
            //System.out.printf("%d %d %d %d %d\n", idx, curAns, prefixOne[idx], totalZero, prefixZero[idx]);
            ans = Math.min(curAns, ans);
        }
        ans = Math.min(totalZero, ans);
        return ans;
    }
}