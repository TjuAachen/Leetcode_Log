class Solution {
    public int longestConsecutive(int[] nums) {
        //@input : nums
        //@output : length of longest consecutive elements
        //@edge case : null, 0
        //@breaking down problem:
        //1.dp set as the longest so far
        //2.traverse the element nums[i], find dp[nums[i-1]], dp[nums[i+1]] if they exists
        //3.then update the head, tail of the sequence
        Map<Integer, Integer> longestSequence = new HashMap<>();
        int ans = 0;
        for(int num : nums){
            int temp = 0;
            int left = 0, right = 0;
            if(longestSequence.containsKey(num))continue;
            if(longestSequence.containsKey(num - 1)){
                left = longestSequence.get(num - 1);
                }
            if(longestSequence.containsKey(num+1)){
                right = longestSequence.get(num + 1);
            }
            temp = left + right + 1;
            longestSequence.put(num, temp);
            if(left != 0){
                longestSequence.put(num - left, temp);
            }
            if(right != 0){
                longestSequence.put(num + right, temp);
            }
            
            ans = Math.max(ans, temp);
        }
        return ans;
    }
}
