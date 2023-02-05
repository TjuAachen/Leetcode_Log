class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] target = new int[26];
        int[] cur = new int[26];
        int n = p.length();
        int sLen = s.length();
        
        if (sLen < n)
            return new LinkedList<>(); 
        
        countChar(s, p, cur);
        countChar(p, p, target);
        int count = 0;
        List<Integer> res = new LinkedList<>();
        
        for (int j = 0; j < 26; j++) {
            if (target[j] == cur[j])
                count++;
        }

        for (int i = 0; i < sLen - n; i++) {
            if (count == 26)
                res.add(i);
            int left = i;
            int right = i + n;
            int leftCharIdx = s.charAt(left) - 'a';
            int rightCharIdx = s.charAt(right) - 'a';
            
            count = updateCount(target, cur, leftCharIdx, rightCharIdx, count);
            
            cur[rightCharIdx]++;
            cur[leftCharIdx]--;
        }
        
        if (count == 26)
            res.add(sLen - n);
        
        return res;
        
    }
    
    public int updateCount(int[] target, int[] cur, int leftCharIdx, int rightCharIdx, int count) {
        if (leftCharIdx != rightCharIdx) {
            if (target[leftCharIdx] == cur[leftCharIdx]) {
                count--;
            }else if (target[leftCharIdx] == cur[leftCharIdx] - 1) {
                count++;
            }
            if (target[rightCharIdx] == cur[rightCharIdx]) {
                count--;
            }else if (target[rightCharIdx] == cur[rightCharIdx] + 1) {
                count++;
            }                
        }
        
        return count;
    }
    
    public void countChar(String s, String p, int[] res) {
        int n = p.length();
        
        for (int i = 0; i < n; i++) {
            char curChar = s.charAt(i);
            int idx = curChar - 'a';
            res[idx] += 1;
        }
    }
}