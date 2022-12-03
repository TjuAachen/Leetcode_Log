class Solution {
    public String alienOrder(String[] words) {
        
        
        Map<Character, Set<Character>> graph = new HashMap<>();
        Set<Character> visited = new HashSet<>();
        
        
        if(!buildGraph(words, graph, visited)){
            return "";
        }
        
        //BFS, topological sort
        StringBuilder res = new StringBuilder();
        
        LinkedList<Character> queue = new LinkedList<>();
        
        Map<Character, Integer> degree = new HashMap<>();
        
        for(int i = 0; i < 26; i++){
            char curChar = (char)('a' + i);
            
            if(!visited.contains(curChar))
                continue;
            degree.computeIfAbsent(curChar, k -> 0);
            if(!graph.containsKey(curChar))
                continue;
            for(Character nxt : graph.get(curChar)){
                
                degree.computeIfAbsent(nxt, k -> 0);
                degree.put(nxt, degree.get(nxt) + 1);
            }
        }
        
        for(int i = 0; i < 26; i++){
            char curChar = (char)('a' + i);
            if(!degree.containsKey(curChar))
                continue;    
            if(degree.get(curChar) == 0){
                queue.addLast(curChar);
            }
            
        }
        
        while(!queue.isEmpty()){
            
            char curNode = queue.pollFirst();
            res.append(curNode);
            
            if(!graph.containsKey(curNode))
                continue;
            
            for(Character node : graph.get(curNode)){
                degree.put(node, degree.get(node) - 1);
                if(degree.get(node) == 0){
                    queue.addLast(node);
                }
            }
        }
        

        if(res.length() == visited.size())
            return res.toString();
        
        return "";
        
        
        
        
        
    }
    
    public boolean buildGraph(String[] words, Map<Character, Set<Character>> graph, Set<Character> visited){
        
        int num = words.length;
        
        for(int i = 0; i < num; i++){
            String curWord = words[i];
            String nxtWord = "";
            
            for(int j = 0; j < curWord.length(); j++){
                char m = curWord.charAt(j);
                visited.add(m);
            }
            
            if(i < num - 1)
                nxtWord = words[i + 1];
            
          //  addEdgesFromWord(curWord, graph);
            if(!addEdgesFromPair(curWord, nxtWord, graph)){
                return false;
            }
        }
        return true;
    }
    
    
    public boolean addEdgesFromPair(String word1, String word2, Map<Character, Set<Character>> graph){
        int p1 = 0;
        int p2 = 0;
        
        int n1 = word1.length();
        int n2 = word2.length();
        
        if(n2 == 0)
            return true;
        
        while(p1 < n1 && p2 < n2){
            char curChar1 = word1.charAt(p1);
            char curChar2 = word2.charAt(p2);
            
            if(curChar1 == curChar2){
                p1++;
                p2++;
            }else{

                graph.computeIfAbsent(curChar1, k -> new HashSet<Character>());
                graph.get(curChar1).add(curChar2);
                return true;
            }
        }
        
        if(p1 == n1 && p2 <= n2)
            return true;
        return false;
        
    }
    
    
    
}