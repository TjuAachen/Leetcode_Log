class Solution {
    public String removeDuplicates(String s) {
        
        StringBuilder Res = new StringBuilder();
        
        for(int i = 0; i < s.length(); i++){
            String temp = s.substring(i, i + 1);
            boolean isSame = false;
            while(!Res.isEmpty() && Res.substring(Res.length() - 1, Res.length()).equals(temp)){
                Res.setLength(Res.length() - 1);
                isSame = true;
            }
            if(!isSame){
            Res.append(temp);
            }
        }
        
        return Res.toString();
        
        
        
    }
}