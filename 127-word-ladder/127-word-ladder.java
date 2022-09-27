class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        //build the graph
        
        HashMap<String, Set<String>> graph = new HashMap<>();
        
        boolean flag = buildGraph(beginWord, endWord, wordList, graph);
        if(!flag)return 0;
        
        LinkedList<LinkedList<String>> queue = new LinkedList<>();
        
        Map<String, Set<String>> prevNodes = new HashMap<>();
        Map<String, Integer> distance = new HashMap<>();
        buildDistance(graph, beginWord, prevNodes, distance);
        return distance.getOrDefault(endWord, 0);
    
    }

    
    
    
    public void buildDistance(Map<String, Set<String>> graph, String beginWord, Map<String, Set<String>> prevNodes, Map<String, Integer> distance){
        LinkedList<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        int step = 1;
        queue.add(beginWord);
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
            String popped = queue.pollFirst();
            distance.put(popped, step);
            for(String modified : modifyString(popped)){
                if(!graph.containsKey(modified))continue;
                for(String nxt : graph.get(modified)){
                    if(distance.containsKey(nxt))continue;
                    if(!visited.contains(nxt)){
                        queue.addLast(nxt);
                        visited.add(nxt);
                    }
                    prevNodes.computeIfAbsent(nxt, k->new HashSet<>());
                    prevNodes.get(nxt).add(popped);
                }
            }
            }
            step += 1;
        }
    }
    public String[] modifyString(String original){
        int n = original.length();
        String[] res = new String[n];
        for(int i = 0; i < n; i++){
            StringBuilder target = new StringBuilder();
            target.append(original.substring(0, i));
            target.append("*");
            target.append(original.substring(i+1));
            res[i] = target.toString();
        }
        return res;
    }
    public boolean buildGraph(String beginWord, String endWord, List<String> wordList, HashMap<String, Set<String>> graph){
        wordList.add(beginWord);
        boolean flag = false;
        for(String word : wordList){
            if(word.equals(endWord)){
                flag = true;
            }
            String[] modifiedStrings = modifyString(word);
            for(String modifiedString : modifiedStrings){
                graph.computeIfAbsent(modifiedString, k -> new HashSet<String>());
                graph.get(modifiedString).add(word);
            }
        }
        return flag;
        
    }
    
}