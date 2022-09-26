class union_set{
    int[] parent = new int[26];
    int[] size = new int[26];
    union_set(){
        for(int i = 0; i < 26; i++){
            parent[i] = i;
            size[i] = 1;
        }
    }
    public int find(int i){
        if(parent[i] == i)return i;
        parent[i] = find(parent[i]);
        return parent[i];
    }
    public void union(int i, int j){
        int parentI = parent[i], parentJ = parent[j];
        if(parentI == parentJ)return;
        if(size[parentI] < size[parentJ]){
            parent[parentI] = parentJ;
            size[parentJ] += size[parentI];
        }else{
            parent[parentJ] = parentI;
            size[parentI] += size[parentJ];
        }
    }
}
class Solution {
    public boolean equationsPossible(String[] equations) {
        //@input : an array of equation string
        //equation string variable1 !=/== variable2
        
        //@output : true or false whether it is self-inconsistent
        //edge case : irregular input
        
        //breaking down problem:
        //1. union find to record the given relationship
        //2. parse the given string if == : union; if != : decide if share the same parent, if true return false
        union_set relation = new union_set();
        HashSet<Pair> visited = new HashSet<>();
        for (String equation : equations){
            if(equation.charAt(1) == '!')continue;
            if (!processEquation(equation, relation, visited))return false;
        }
        for (String equation : equations){
            if(equation.charAt(1) == '=')continue;
            if (!processEquation(equation, relation, visited))return false;
        }
        return true;
        
    }
    public boolean processEquation(String equation, union_set relation, Set visited){
        int v1 = equation.charAt(0) - 'a', v2 = equation.charAt(3) - 'a';
        int parent1 = relation.find(v1), parent2 = relation.find(v2);
        
        Pair key = new Pair(Math.max(v1,v2), Math.min(v1,v2));
        if(equation.charAt(1) == '='){
            if(visited.contains(key)&& parent1 != parent2)return false;
            relation.union(v1, v2);
        }else if(parent1 == parent2){
            return false;
        }
        visited.add(key);
        return true;
    }
    
}