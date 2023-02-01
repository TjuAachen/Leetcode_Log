class Solution {
    public String gcdOfStrings(String str1, String str2) {
        LinkedHashSet<String> gcd1 = findGCD(str1);
        LinkedHashSet<String> gcd2 = findGCD(str2);
        String res = "";
        
        for (String element : gcd1) {
            if (gcd2.contains(element))
                res = element;
        }
        
        return res;
    }
    
    public LinkedHashSet<String> findGCD(String str) {
        int n = str.length();
        LinkedHashSet<String> res = new LinkedHashSet<>();
        
        for (int i = 0; i < n; i++) {
            int gcdLength = i + 1;
            if (n % gcdLength != 0)
                continue;
            if (isGCD(gcdLength, str)) {
                res.add(str.substring(0, gcdLength));
            }
        }
        
        return res;
    }
    
    public boolean isGCD(int blockLength, String str) {
        int n = str.length();
        
        for (int i = 0; i < n; i += blockLength) {
            String curStr = str.substring(i, i + blockLength);
            if (!curStr.equals(str.substring(0, blockLength)))
                return false;
        }
        
        return true;
        
    }
}