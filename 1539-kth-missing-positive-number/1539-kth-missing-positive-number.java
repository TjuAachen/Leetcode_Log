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
   //     System.out.printf("%d %d\n", left, right);
        if (arr[right] - right - 1 < k)
            return right + k + 1;
        if (arr[left] - left - 1 < k) {
            return left + k + 1;
        }
        return k;

}
}