class Solution {
    private Map<Character, String> digitToLetter = Map.of('2', "abc", '3', "def", '4', "ghi", '5', "jkl", 
        '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz");
    private List<String> combinations = new ArrayList<>();
    public List<String> letterCombinations(String digits) {
        if(digits .equals("")) return combinations;
        
        this.findAllString(digits, new StringBuilder());
        
        
        
        return combinations;
    }
    public void findAllString(String digits, StringBuilder path){
        if(digits.length() == 0){
            combinations.add(path.toString());
            return;
        }
        char cur_digit = digits.charAt(0);
        String letters = digitToLetter.get(cur_digit);
        for(char letter : letters.toCharArray()){
            path.append(letter);
            this.findAllString(digits.substring(1), path);
            path.deleteCharAt(path.length() - 1);
        }
    }
}