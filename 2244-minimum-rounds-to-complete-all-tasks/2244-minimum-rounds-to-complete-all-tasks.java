class Solution {
    int option1 = 3;
    int option2 = 2;
    
    public int minimumRounds(int[] tasks) {
        Map<Integer, Integer> difficultyNum = new HashMap<>();
        int ans = 0;
        
        for (int task : tasks){
            difficultyNum.computeIfAbsent(task, k -> 0);
            difficultyNum.put(task, difficultyNum.get(task) + 1);
        }
        
        for (Map.Entry<Integer, Integer> entry : difficultyNum.entrySet()){
            int curRoundCount = minimumRound(entry.getValue());
            if (curRoundCount == -1)
                return -1;
            ans += curRoundCount;
        }
        
        return ans;
    }
    
    public int minimumRound(int count){

        int factorOf3 = count / option1;
        int remaining = count - factorOf3 * option1;
        
        if (remaining != 1)
            return factorOf3 + remaining / 2;
        if (factorOf3 > 0)
            return factorOf3 + 1;
        return -1;
        
    }
}