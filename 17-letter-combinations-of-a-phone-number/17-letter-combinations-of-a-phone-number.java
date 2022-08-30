class Solution {
    public List<String> letterCombinations(String digits) {
        HashMap<Character, char[]> digitToLetter = new HashMap<>(){{put('2',new char[]{'a','b','c'});put('3',new char[]{'d','e','f'});
put('4',new char[]{'g','h','i'}); put('5',new char[]{'j','k','l'});
put('6',new char[]{'m','n','o'}); put('7',new char[]{'p','q','r', 's'}); put('8',new char[]{'t','u','v'}); put('9',new char[]{'w','x','y','z'});                                                 }};
        if(digits .equals("")) return new LinkedList<>();
        List<String> res = new LinkedList<>();
        List<StringBuilder> ans = this.findAllString(digits, digitToLetter);
        for(StringBuilder elem : ans){
            res.add(elem.toString());
        }
        return res;
    }
    public List<StringBuilder> findAllString(String digits, HashMap<Character, char[]> digitToLetter){
        
        List<StringBuilder> ans = new LinkedList<>();
        
        if(digits.equals("")) return ans;
        
        char cur_digit = digits.charAt(0);
        char[] letters = digitToLetter.get(cur_digit);
        List<StringBuilder> temp_res  = this.findAllString(digits.substring(1), digitToLetter);
        for(char letter : letters){
            if (temp_res.isEmpty()){
                ans.add(new StringBuilder(Character.toString(letter)));
            }else{
            for(StringBuilder combos : temp_res){
                StringBuilder temp_combo = new StringBuilder(combos.toString());
                temp_combo.insert(0, letter);
                ans.add(temp_combo);
            }
            }
            
        }
        
        return ans;
    }
}