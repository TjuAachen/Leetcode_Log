class Solution {
    public String pushDominoes(String dominoes) {
        //@input : a string of dominoes in the initial state
        //@output : final state of dominoes with . state is decided
        //@breaking down the problem:
        //1. traverse each domino with '.' and decide its state
        //1.0 traverse the dominoes to figure out which states are unset
        //1.1 traverse by BFS
        //1.2 in the same level, if the state is originally unset and currently set, then set it as specified
        //1.3 in the same level, if the state is not set, then set it as specified
        LinkedList<int[]> queue = new LinkedList<>();
        buildQueue(dominoes, queue);
        int n = dominoes.length();
        char[] characters = dominoes.toCharArray();
        //bfs
        while(!queue.isEmpty()){
            int size = queue.size();
            Set<Integer> newlySet = new HashSet<>();
            for(int i = 0; i < size; i++){
                int[] popped = queue.pollFirst();
                //if left
                if(popped[1] == 0){
                    if(popped[0] > 0 && characters[popped[0] - 1] == '.'){
                        if(popped[0] == 1 || characters[popped[0] - 2] == '.' || characters[popped[0] - 2] == 'L' || (characters[popped[0] - 2] == 'R' && newlySet.contains(popped[0] - 2))){
                            characters[popped[0] - 1] = 'L';
                            newlySet.add(popped[0] - 1);
                            queue.addLast(new int[]{popped[0] - 1, 0});
                        }
                    }
                }else{
                    if(popped[0] < n - 1&& characters[popped[0] + 1] == '.'){
                        if(popped[0] == n - 2 || characters[popped[0] + 2] == '.' || characters[popped[0] + 2] == 'R' ||  (characters[popped[0] + 2] == 'L' && newlySet.contains(popped[0] + 2))){
                            characters[popped[0] + 1] = 'R';
                            newlySet.add(popped[0] + 1);
                            queue.addLast(new int[]{popped[0] + 1, 1});
                        }
                    }                    
                }
                
            }
        }
        String res = String.copyValueOf(characters);
        return res;
        
        
        
        
    }
    public void buildQueue(String dominoes, LinkedList<int[]> queue){
        for(int i = 0; i < dominoes.length(); i++){
            char curChar = dominoes.charAt(i);
            int n = dominoes.length();
            if(curChar == '.'){
                continue;
            }else if(curChar == 'L' && i > 0 && dominoes.charAt(i-1) == '.'){
                //0 : L, 1 : R
                int[] elem = new int[]{i, 0};
                queue.addLast(elem);
            }else if(curChar == 'R'  && i < n - 1 && dominoes.charAt(i+1) == '.'){
                int[] elem = new int[]{i, 1};
                queue.addLast(elem);                
            }
        }
    }
}