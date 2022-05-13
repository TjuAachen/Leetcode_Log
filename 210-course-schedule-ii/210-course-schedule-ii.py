class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = dict()
        result = dict()
        visited = dict()
        path = dict()
        final = []
        global hasCycle
        hasCycle = False
        
        record = dict()
        for pre in prerequisites:
            a, b = pre
            if a not in record:
                record[a] = [b]
            else:
                record[a].append(b)
        
        def traverse(start):
            global hasCycle
            if start in path:
                hasCycle = True
                return
            if start in visited or hasCycle:
                return
            visited[start] = 1
            if start not in record:
                final.append(start)
                return
            path[start] = 1
            for pre in record[start]:
                traverse(pre)
            if not hasCycle:
                final.append(start)
            del path[start]
        for course in range(numCourses):
            traverse(course)
        if not hasCycle:
            return final
        return []