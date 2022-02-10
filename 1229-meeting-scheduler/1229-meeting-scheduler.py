class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        n1, n2 = len(slots1), len(slots2)
        i, j = 0, 0
        res = []
        start, end = [], []
        count = 0
        slot = slots1 + slots2
        slot.sort()
        for k in slot:
            start.append(k[0])
            end.append(k[1])
        end.sort()
        while(i<n1+n2 and j<n1+n2):
            if start[i] < end[j]:
                count += 1
                i += 1
            elif start[i] > end[j]:
                count -= 1
                j += 1
            else:
                i += 1
                j += 1
            if count == 2 and  end[j]-start[i-1]>=duration:
                return [start[i-1], start[i-1]+duration]
        return []
                
            
        