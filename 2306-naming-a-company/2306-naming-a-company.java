class Solution {
    public long distinctNames(String[] ideas) {
        Set<String> ideaSet = new HashSet<>();
        Map<Integer, List<String>> initialToString = new HashMap<>();
        int[][] iTojCount = new int[26][26];
        
        for (int i = 0; i < 26; i++) {
            initialToString.put(i, new LinkedList<String>());
        }
        long res = 0;
        for (String idea : ideas) {
            char curInit = idea.charAt(0);
            initialToString.get(curInit - 'a').add(idea);
            ideaSet.add(idea);
        }
        
        for (int i = 0; i < 26; i++) {
            for (String candidate : initialToString.get(i))
                for (int j = 0; j < 26; j++) {
                    if (i == j)
                        continue;
                    String newInitialStr = String.valueOf((char) (j + 'a'));
                    String changedStr = newInitialStr + candidate.substring(1, candidate.length());
                   // System.out.printf("%d %d %s\n", i, j, changedStr);
                    if (!ideaSet.contains(changedStr))
                        iTojCount[i][j] += 1;
            }
        }
        
        for (int i = 0; i < 26; i++)
            for (int j = 0; j < 26; j++) {
               // System.out.printf("%d %d %d\n", i, j, iTojCount[i][j]);
                 res += iTojCount[i][j] * iTojCount[j][i];
            }
        
        return res;
        
        
        
        
        
        
    }
}