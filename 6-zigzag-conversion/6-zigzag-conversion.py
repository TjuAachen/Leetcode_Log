class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = defaultdict(list)
        numList = [i for i in range(numRows)]
        numList_reversed = numList[::-1]
        numList = numList + numList_reversed[1:-1]
        queue = deque(numList)
        for char in s:
            popped = queue.popleft()
            res[popped].append(char)
            queue.append(popped)
        result = ''
        for i in range(numRows):
            result += ''.join(res[i])
        return result
            
        
            
            
            
        