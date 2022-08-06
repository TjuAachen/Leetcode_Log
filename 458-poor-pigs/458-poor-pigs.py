class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        num_of_tests = minutesToTest // minutesToDie
        x = 0
        while((num_of_tests + 1)**x < buckets):
            x = x + 1
        return x
        