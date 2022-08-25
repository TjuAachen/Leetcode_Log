class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        Deque<Integer> q = new LinkedList<>();
        int N = s.length();
        q.offerLast(0);
        boolean[] visited = new boolean[N];
        for(int i = 0; i < N && i!=-1; i = s.indexOf('0',i+1)){
            while(!q.isEmpty() && i - q.peek() > maxJump ) q.poll();
            if(!q.isEmpty() && i - q.peek() >= minJump){
                q.offer(i);
                if (i == N - 1) return true;
            }
            if (q.isEmpty())return false;
        }
        return false;
    }
    
}