class Solution {
    public int findKthPositive(int[] arr, int k) {
        int expNum = 1;
        
        if (arr[arr.length - 1] == arr[0] + arr.length - 1 && arr[0] == 1) {
            return arr[arr.length - 1] + k;
        }
        
        for (int num : arr) {
            if (num == expNum) {
                expNum += 1;
                continue;
            }
            int missingCount = num - expNum;
            if (missingCount < k) {
                k -= missingCount;
                expNum = num + 1;
                continue;
            }
            break;
        }
        
        return expNum + k - 1;
        
        
    }
}