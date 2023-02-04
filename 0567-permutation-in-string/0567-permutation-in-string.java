class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        if (n1 > n2)
            return false;
        int[] map1 = new int[26];
        int[] map2 = new int[26];
        
        for (int i = 0; i < n1; i++) {
            int curIdx1 = s1.charAt(i) - 'a';
            int curIdx2 = s2.charAt(i) - 'a';
            map1[curIdx1] += 1;
            map2[curIdx2] += 1;
        }
        
        int count = 0;
        for (int j = 0; j < 26; j++) {
            if (map1[j] == map2[j])
                count++;
        }
        
        
        
        int left = 0;
        int right = 0;
        //fixed window length
        for (int i = 0; i < n2 - n1; i++) {
            int r = s2.charAt(i + n1) - 'a';
            int l = s2.charAt(i) - 'a';
            
            if (count == 26)
                return true;
            if (l != r) {
            if (map1[l] == map2[l])
                count -= 1;
            else if (map1[l] == map2[l] - 1)
                count += 1;
            if (map1[r] == map2[r] + 1)
                count += 1;
            else if (map1[r] == map2[r])
                count -= 1;
            }
            map2[r] += 1;
            map2[l] -= 1;
        }
        
        return count == 26;
        
    }
    

}