class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #greedy algorithm
        left, right = 0, len(numbers) - 1
        while(left < right):
            temp = numbers[left] + numbers[right]
            if temp == target:
                return [left + 1, right + 1]
            if temp < target:
                left = left + 1
            else:
                right = right - 1
            
        
                