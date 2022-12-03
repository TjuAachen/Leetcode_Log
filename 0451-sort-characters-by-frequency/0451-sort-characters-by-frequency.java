class Solution {
    public String frequencySort(String s) {
        
        Map<Character, Integer> wordFreq = new HashMap<>();
        
        for (char cur : s.toCharArray()){
            wordFreq.computeIfAbsent(cur, k -> 0);
            wordFreq.put(cur, wordFreq.get(cur) + 1);
        }
        
        PriorityQueue<Pair<Integer, Character>> pq = new PriorityQueue<>((a, b) -> b.getKey() - a.getKey());
        
        for (Map.Entry<Character, Integer> entry : wordFreq.entrySet()){
            Pair<Integer, Character> pair = new Pair<>(entry.getValue(), entry.getKey());
            pq.add(pair);
        }
        
        StringBuilder res = new StringBuilder();
        
        while(!pq.isEmpty()){
            Pair<Integer, Character> popped = pq.poll();
            
            for (int i = 0; i < popped.getKey(); i++)
                res.append(String.valueOf(popped.getValue()));
        }
        
        return res.toString();
        
        
        
        
        
        
    }
}