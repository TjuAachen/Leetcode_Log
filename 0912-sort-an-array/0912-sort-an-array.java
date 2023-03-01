class Solution {
    public int[] sortArray(int[] nums) {
        // quick sort
        quickSort(nums, 0, nums.length - 1);
        
        return nums;
        
    }
    public void quickSort(int[] nums, int start, int end) {
        if (start >= end) {
            return;
        }
        
        int left = start;
        int right = end;
        int pivot = nums[left + (right - left) / 2];
        
        while (left <= right) {
            while (left <= right && nums[left] < pivot) {
                left++;
            }
            while (left <= right && nums[right] > pivot) {
                right--;
            }
            
            if (left <= right) {
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;
                left++;
                right--;
            }
        }
        quickSort(nums, start, right);
        quickSort(nums, left, end);
    }
}