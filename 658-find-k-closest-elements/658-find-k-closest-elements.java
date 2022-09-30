class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        //@input : arr of integer
        //@output : list of integers closest to integer x
        //@edge case : illegal input
        //@breaking down problem:
        //1. binary search to find cloest to x
        //2. set left, right pointer to the left, right of x
        //3. add the cloest one between two into the linkedlist 
        int leftIdx = findLeftBoundary(arr, k, x);
        LinkedList<Integer> res = new LinkedList<>();
        for(int i = leftIdx; i < leftIdx + k; i++){
            res.add(arr[i]);
        }
        return res;
        
        
        
        

    

    }
    public int findLeftBoundary(int[] arr, int k, int x){
        int left = 0, right = arr.length - k;
        //正着推得能得到什么条件，不满足则排除。二分法理解为排除法
        while(left < right){
            int mid = left + (right - left) / 2;
            if(Math.abs(arr[mid] - x) < Math.abs(arr[mid + k] - x)){
                right = mid;
            }else if (Math.abs(arr[mid] - x) > Math.abs(arr[mid + k] - x)){
                left = mid + 1;
            }else if (arr[mid + k] < x){
                left = mid + 1;
            }else {
                right = mid;
            }
        }
        return left;
    }
}
    
    
