class Solution {
    int BASE = 100000;
    public int strStr(String haystack, String needle) {
        if (haystack == null || needle == null)
            return -1;
        
        int max = needle.length();
        
        //31^m
        int power = 1;
        for (int i = 0; i < max; i++){
            power = (power * 31) % BASE;
        }
        
        int targetCode = 0;
        for (int i = 0; i < max; i++){
            targetCode = (targetCode * 31 + needle.charAt(i)) % BASE;
        }
        
        int hashCode = 0;
        for (int i = 0; i < haystack.length(); i++){
            // abc + d
            hashCode = (hashCode * 31 + haystack.charAt(i)) % BASE;
            if (i < max - 1)
                continue;
            
            if (i >= max){
                hashCode = hashCode - (haystack.charAt(i - max) * power) % BASE;
                if (hashCode < 0)
                    hashCode += BASE;
            }
            
            //double check the string
            if (hashCode == targetCode){
                if (haystack.substring(i - max + 1, i + 1).equals(needle))
                    return i - max + 1;
            }
        }
        
        return -1;
    }

}