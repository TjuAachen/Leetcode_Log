class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        answer = []
        for i in intervals:
            if i[1] <= toBeRemoved[0]:
                answer.append(i)
            elif i[0] < toBeRemoved[0]:
                answer.append([i[0],toBeRemoved[0]])
            if i[0] >= toBeRemoved[1]:
                answer.append(i)
            elif i[1] > toBeRemoved[1]:
                answer.append([toBeRemoved[1],i[1]])
        return answer