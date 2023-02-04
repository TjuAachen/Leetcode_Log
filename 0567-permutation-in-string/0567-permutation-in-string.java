class Solution {
    public boolean checkInclusion(String s1, String s2) {
        String sortedS1 = sortedString(s1);
        int n1 = s1.length();
        int n2 = s2.length();
        
        for (int i = 0; i <= n2 - n1; i++) {
            String cur = s2.substring(i, i + n1);
            String sortedCur = sortedString(cur);
            if (sortedCur.equals(sortedS1))
                return true;
        }
        
        return false;
        
        
    }
    
    public String sortedString(String s1) {
        char [] c = s1.toCharArray();
        Arrays.sort(c);
        String sortedS1 = new String(c);
        return sortedS1;
    }
}