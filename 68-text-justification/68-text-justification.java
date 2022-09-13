class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        //each line
        LinkedList<String> res = new LinkedList<>();
        int i = 0;
        int wordNum = words.length;
        int tempLen = 0;
        List<String> temp = new LinkedList<>();
        while(i < wordNum){
            tempLen = 0;
            temp = new LinkedList<>();
            while(i < wordNum && tempLen + words[i].length() + temp.size()<= maxWidth){
                tempLen += words[i].length();
                temp.add(words[i++]);
            }
            res.addLast(arrangeLine(temp, maxWidth - tempLen));
        }
        res.pollLast();
        //final line
        StringBuilder curRes = new StringBuilder();
        int remaining = maxWidth - tempLen;
        for(String elem : temp){
            curRes.append(elem);
            if (remaining > 0){
                curRes.append(" ");
                remaining--;
            }
        }
        while(remaining > 0){
            curRes.append(" ");
            remaining--;
        }
        res.addLast(curRes.toString());
        
        return res;
    }
    public String arrangeLine(List<String> words, int emptyWidth){
        int len = words.size();
        StringBuilder res = new StringBuilder();
        if(len == 1){
            res.append(words.get(0));
            while(emptyWidth > 0){
                res.append(" ");
                emptyWidth--;
            }
            return res.toString();
        }
        
        int[] blanks = new int[len - 1];
        int average = emptyWidth / (len - 1);
        int remaining = emptyWidth%(len - 1);
        int i = 0;
        for(i = 0; i < blanks.length;i++){
            blanks[i] = average;
        }
        i = 0;
        while(remaining > 0){
            blanks[i++] += 1;
            remaining--;
        }
        
        for(int j = 0; j < len; j++){
            res.append(words.get(j));
            while(j < len - 1 && blanks[j] > 0){
                res.append(" ");
                blanks[j]-=1;
            }
        }
     return res.toString();   
    }
}