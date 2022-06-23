from heapq import *
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        queue = []
        choice = []
        heapify(queue)
        heapify(choice)
        for course in courses:
            modified_course = [course[-1], course[0]]
            heappush(queue, modified_course)
        count = 0
        cur_start = 1
        while(queue):
            top = heappop(queue)
            if cur_start + top[1] - 1 <= top[0]:
                count += 1
                cur_start = cur_start + top[1]
                heappush(choice, [-top[1], top[0]])
            elif choice and -choice[0][0] > top[1]:
                cur_start = cur_start +choice[0][0]+top[1]
                heappop(choice)
                heappush(choice, [-top[1], top[0]])
        return count