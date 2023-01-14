class union_set {
    int[] parent = new int[26];
    int[] size = new int[26];
    
    union_set() {
        for (int idx = 0; idx < 26; idx++) {
            size[idx] = 1;
            parent[idx] = idx;
        }
    }
    
    public void union(int p, int q) {
        int parentP = find(p), parentQ = find(q);
        if (parentP == parentQ)
            return;
        if (size[p] <= size[q]) {
            parent[parentP] = parentQ;
            size[q] += size[p];
            return;
        }
        
        parent[parentQ] = parentP;
        size[p] += size[q];
    }
    
    public int find(int p) {
        if (p == parent[p])
            return p;
        
        parent[p] = find(parent[p]);
        
        return parent[p];
    }
}
class Solution {
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        int n = s1.length();
        int baseStrLen = baseStr.length();
        union_set unionSet = new union_set();
        
        for (int idx = 0; idx < n; idx++) {
            int idx1 = s1.charAt(idx) - 'a';
            int idx2 = s2.charAt(idx) - 'a';
            unionSet.union(idx1, idx2);
        }
        
        StringBuilder ans = new StringBuilder();
        for (int idx = 0; idx < baseStrLen; idx++) {
            String curChar = baseStr.substring(idx, idx + 1);
            int charIdx = baseStr.charAt(idx) - 'a';
            int minIdx = Integer.MAX_VALUE;
            int parent = unionSet.find(charIdx);
            
            for (int nxt = 0; nxt < 26; nxt++) {
                String nxtChar = String.valueOf((char) (nxt + 'a'));
                
                if (parent == unionSet.find(nxt)) {
                    ans.append(nxtChar);
                    break;
                }
            }
        }
        
        return ans.toString();
    }
}