class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int N = queries.length;
        int[] res = new int[N];
        int curRes = 0;
        for(int num : nums){
            if(num % 2 == 0){
                curRes += num;
            }
        }
        int i = 0;
        for(int[] query : queries){
            int val = query[0];
            int index = query[1];
            int num = nums[index];
            if(num%2 == 0){
                if((num + val) % 2 == 0){
                    curRes += val;
                }else{
                    curRes -= num;
                }
                nums[index] += val; 
            }else{
                if((num + val) % 2 == 0){
                    curRes += num + val;
                }
                nums[index] += val; 
            }
            res[i++] = curRes;
        }
        return res;
        
        
    }
}