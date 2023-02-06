class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] res = new int[2 * n];
        int xPointer = 0;
        int yPointer = n;
        for (int i = 0; i < 2 * n; i++) {
            if (i % 2 == 0) {
                res[i] = nums[xPointer++];
            } else {
                res[i] = nums[yPointer++];
            }
        }
        
        return res;
    }

}