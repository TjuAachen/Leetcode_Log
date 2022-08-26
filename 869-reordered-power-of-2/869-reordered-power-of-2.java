class Solution {
    public boolean reorderedPowerOf2(int n) {
        int temp = n&(n-1);
        if (temp == 0)
            return true;
        //extract number
        List<Character> digits = new ArrayList<>();
        while(n > 0){
            String temp_string = String.valueOf(n%10);
            char nToChar = temp_string.charAt(0);
            digits.add(nToChar);
            n /= 10;
        }
        HashSet<String> powerOfTwo = new HashSet<>();
        Collections.sort(digits);
        int num = 1;
        while(num <= Math.pow(10, 9)){
            String inputString = String.valueOf(num);
            char tempArray[] = inputString.toCharArray();
            Arrays.sort(tempArray);
            powerOfTwo.add(new String(tempArray));
            num = (num << 1);
        }
    //    String standard = new String(digits);
        StringBuilder builder = new StringBuilder(digits.size());
        
        for(char elem : digits){
            builder.append(elem);
        }
        
        if(powerOfTwo.contains(builder.toString())){
            return true;
        }
        return false;
        
        
    }
}