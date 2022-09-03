class Solution {
    public int strStr(String haystack, String needle) {
        int needle_size = needle.length();
        int[] nxt = new int[needle_size];
        
        //KMP nxt matrix
        int j = 2, curCommonLength = 0;
        while(j < needle_size){
            if(needle.charAt(curCommonLength) == needle.charAt(j - 1)){
                curCommonLength++;
                nxt[j++] = curCommonLength;
            }else if(curCommonLength > 0){
                curCommonLength = nxt[curCommonLength];
            }else{
                nxt[j++] = 0;
            }    
        }
        int k = 0;
        int i = 0;
        while(i < haystack.length()){
            if(haystack.charAt(i) != needle.charAt(k)){
                if(k == 0)i++;
                k = nxt[k];
            }else if (k == needle_size - 1){
                return i - k;
            }else{
                k++;
                i++;
            
            }
          //  System.out.printf("%d %d\n",i,k);
            
        }

        return -1;
    }

}