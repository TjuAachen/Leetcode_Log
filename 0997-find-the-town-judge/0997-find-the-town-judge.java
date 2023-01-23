class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] score = new int[n];
        
        for (int[] curTrust : trust) {
            int start = curTrust[0];
            int end = curTrust[1];
            score[start - 1] -= 1;
            score[end - 1] += 1;
        }
        
        for (int i = 0; i < n; i++) {
            if (score[i] == n - 1)
                return i + 1;
        }
        
        return -1;
        
    }
}