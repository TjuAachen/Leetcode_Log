class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        //@input : arr of integer
        //@output : list of integers closest to integer x
        //@edge case : illegal input
        //@breaking down problem:
        //1. binary search to find cloest to x
        //2. set left, right pointer to the left, right of x
        //3. add the cloest one between two into the linkedlist 
        LinkedList<Integer> res = new LinkedList<>();
        int idx = binarySearch(arr, x);
        int left = idx - 1, right = idx + 1;
        res.add(arr[idx]);
        k = k - 1;
        int n = arr.length;
        while(k > 0 &&(left >= 0 || right < n)){
            int leftVal = -50001, rightVal = -50001;
            if(left >= 0){
                leftVal = arr[left];
            }
            if(right < n){
                rightVal = arr[right];
            }
            if(Math.abs(leftVal - x) <= Math.abs(rightVal -x)){
                res.addFirst(leftVal);
                left--;
            }else if(Math.abs(leftVal - x) > Math.abs(rightVal -x)){
                res.addLast(rightVal);
                right++;
            }
            k--;
            
        }
        return res;
        
        
        
    }
    public int binarySearch(int[] arr, int x){
        int left = 0, right = arr.length - 1;
        while(left < right - 1){
            int mid = left + (right - left) / 2;
            if(arr[mid] == x){
                return mid;
            }else if(arr[mid] < x){
                
                if(arr[mid + 1] > x){
                    if(x - arr[mid] <= arr[mid + 1] - x){
                        return mid;
                    }
                    return mid+1;
                }
                left = mid + 1;
            }else{
                if(arr[mid - 1] < x){
                    if(x - arr[mid - 1] <= arr[mid] - x){
                        return mid - 1;
                    }
                    return mid;
                }
                right = mid - 1;                    
                }
            }
            int leftVal = arr[left], rightVal = arr[right];
            if(Math.abs(leftVal - x) <= Math.abs(rightVal -x)){
                return left;
            }
        return right;
        }
    
}
    
    
