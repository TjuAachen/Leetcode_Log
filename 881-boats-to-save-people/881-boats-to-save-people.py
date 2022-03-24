class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left, right = 0, len(people) - 1
        time = 0
        while(left <= right):
            exp = limit - people[left]
            while(right > left and people[right] > exp):
                time = time + 1
                right = right - 1
            if right >= left:
                time = time + 1
                left = left + 1
                right = right - 1
        return time
                
                
            