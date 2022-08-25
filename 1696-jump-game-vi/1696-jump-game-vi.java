class Solution {
    public int maxResult(int[] nums, int k) {
        int N = nums.length;
        int[] score = new int[N];
        Deque<Integer> queue = new LinkedList<>();
        queue.offerLast(0);
        score[0] = nums[0];
        for(int i = 0; i < N - 1; i++){
            //update the queue
            while(!queue.isEmpty() && i - queue.peekFirst() >= k) queue.pollFirst();
            while(!queue.isEmpty() && score[queue.peekLast()] <= score[i]) queue.pollLast();
            queue.offerLast(i);
            score[i+1] = score[queue.peekFirst()] + nums[i+1];
        }
        return score[N-1];
        
    }
}