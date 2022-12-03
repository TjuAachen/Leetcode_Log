class Solution {
    public String alienOrder(String[] words) {
        
        StringBuilder res = new StringBuilder();
        Map<Character, List<Character>> graph = new HashMap<>();
        Map<Character, Integer> degree = new HashMap<>();
        
        
        initialize(graph, degree, words);
        
        if(!buildGraph(graph, degree, words))
            return "";
        
        
        //bfs, topological sorting
        
        LinkedList<Character> queue = new LinkedList<>();
        
        for (Character c : degree.keySet()){
            if (degree.get(c).equals(0))
                queue.add(c);
        }
        
        while(!queue.isEmpty()){
            char popped = queue.pollFirst();
            res.append(popped);
            
            for (Character nxt : graph.get(popped)){
                degree.put(nxt, degree.get(nxt) - 1);
                if(degree.get(nxt) == 0)
                    queue.add(nxt);
            }
        }
        
        if (res.length() == degree.size())
            return res.toString();
        
        return ""; 
    }
        
    public void initialize(Map<Character, List<Character>> graph, Map<Character, Integer> degree, String[] words){
        for (String word : words){
            for (char c : word.toCharArray()){
                degree.put(c, 0);
                graph.put(c, new ArrayList<>());
            }
        }
    
    }
    
    public boolean buildGraph(Map<Character, List<Character>> graph, Map<Character, Integer> degree, String[] words){
        
        for (int i = 0; i < words.length - 1; i++){
            String curWord = words[i];
            String nxtWord = words[i + 1];
            
            if(curWord.length() > nxtWord.length() && curWord.startsWith(nxtWord))
                return false;
            
            for(int k = 0; k < Math.min(curWord.length(), nxtWord.length()); k++){
                char cur = curWord.charAt(k);
                char nxt = nxtWord.charAt(k);
                
                if(cur != nxt){
                    graph.get(cur).add(nxt);
                    degree.put(nxt, degree.get(nxt) + 1);
                    break;
                }
            }
        }
        
        return true;
        
        
    }
    
    

}