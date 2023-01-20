class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        combination(nums, 0, new LinkedList<Integer>(), res, "", visited);
        return res;
    }
    
    public void combination(int[] nums, int start, LinkedList<Integer> curAns, List<List<Integer>> res, String curVal, Set<String> visited) {
      if (curAns.size() >= 2) {
          if (visited.contains(curVal))
              return;
          LinkedList<Integer> temp = new LinkedList<>(curAns);
          visited.add(curVal);
          res.add(temp);
      }
        int prev = - 101;
        for (int idx = start; idx < nums.length; idx++) {
            int num = nums[idx];
            if (nums[idx] == prev)
                continue;
            prev = nums[idx];
            if (curAns.isEmpty() || curAns.peekLast() <= num) {
                String newElement = String.valueOf(num) + "%";
                curVal += newElement;
                curAns.add(num);
                combination(nums, idx + 1, curAns, res, curVal, visited);
                curAns.pollLast();
                curVal = curVal.substring(0, curVal.length() - newElement.length());
            }
        }
    }
}