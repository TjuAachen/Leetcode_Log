class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        record = dict()
        result = dict()
        visited = dict()
        for pre in prerequisites:
            a, b = pre
            if a not in record:
                record[a] = [b]
            else:
                record[a].append(b)
        def find(start):
            if start in result:
                return result[start]
            
            if start not in record:
                result[start] = True
                return True
            
            for pre in record[start]:
                if start == pre or pre in visited:
                    result[pre] = False
                    return False
                visited[pre] = 1
                if not find(pre):
                    return False
                del visited[pre]
            result[start] = True
            return result[start] 
        for course in range(numCourses):
            if not find(course):
                return False
        return True
            
                
                
            
        