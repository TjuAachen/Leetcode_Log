# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity_candidate = 0
        self.n = n
        for i in range(n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i

        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1
    def is_celebrity(self, celebrity_candidate):
        for i in range(self.n):
            if i != celebrity_candidate and (knows(celebrity_candidate, i) or not knows(i, celebrity_candidate)):
                return False
        return True
        
                