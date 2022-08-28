class Solution {
    public String intToRoman(int num) {
        StringBuilder res = new StringBuilder();
        
        Map<Integer, String> valToSym = new TreeMap<>(Collections.reverseOrder()){{
       put(1,"I"); put(5,"V"); put(10, "X"); put(50, "L"); 
        put(100,"C"); put(500,"D"); put(1000, "M"); put(4, "IV"); 
        put(9,"IX"); put(40,"XL"); put(90, "XC"); put(400, "CD");
        put(900,"CM");    
        }};
        
        for (Map.Entry<Integer, String>entry : valToSym.entrySet()){
            int key = entry.getKey();
            String val = entry.getValue();
            int count = num / key;
            num = num - count * key;
            for(int i = 0; i < count; i++)
                res.append(val);
        }
        return res.toString();
    }
}