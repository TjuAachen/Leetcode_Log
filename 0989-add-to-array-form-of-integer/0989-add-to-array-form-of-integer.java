class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        LinkedList<Integer> numList = new LinkedList<>();
        int carry = 0;
        List<Integer> res = new LinkedList<>();
        
        for (int i = 0; i < num.length; i++)
            numList.add(Integer.valueOf(num[i]));
        Collections.reverse(numList);
        
        for (int digit : numList) {
            int temp = digit + k % 10 + carry;
            k /= 10;
            carry = temp / 10;
            res.add(temp % 10);
        }
        
        int temp = k + carry;
        while (temp > 0) {
            res.add((temp) % 10);
            temp /= 10;
            
            }
        Collections.reverse(res);
        return res;
    }
}