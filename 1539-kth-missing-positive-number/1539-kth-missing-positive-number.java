class Solution {
    public int findKthPositive(int[] arr, int k) {
        //binary search
        int left = 0;
        int right = arr.length - 1;
        
        //find the left boundary
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            
            int curCount = arr[mid] - mid - 1;
            
            if (curCount >= k) {
                right = mid;
            }else {
                left = mid;
            }
        }

        if (arr[left] - left - 1 >= k) {
            return calculateMissing(arr, k, left);
        }
        if (arr[right] - right - 1 >= k)
            return calculateMissing(arr, k, right);
        
        return calculateMissing(arr, k, arr.length);
 
    }
    public int calculateMissing(int[] arr, int k, int left) {
        if (left == 0) {
            return k;
        }
        int leftNum = arr[left - 1];
        int prevMissingCount = leftNum - left;
        return leftNum + k - prevMissingCount;
    }
}