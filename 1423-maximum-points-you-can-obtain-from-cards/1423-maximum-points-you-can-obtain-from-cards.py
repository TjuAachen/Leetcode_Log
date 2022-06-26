class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cardsNum = len(cardPoints)
        window_len = cardsNum - k
        subarray = [0] * (cardsNum + 1)
        for i in range(1, cardsNum + 1):
            subarray[i] = subarray[i-1] + cardPoints[i-1]
        
        res = float('inf')
        for start in range(k+1):
            end = start + window_len
            cur = subarray[end] - subarray[start]
            res = min(res, cur)
        return subarray[-1]- res
            