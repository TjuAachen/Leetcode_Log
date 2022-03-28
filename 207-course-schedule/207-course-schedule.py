class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacent = dict()
        for pre in prerequisites:
            if pre[1] not in adjacent:
                adjacent[pre[1]] = [pre[0]]
            else:
                adjacent[pre[1]].append(pre[0])
        path = dict()
        visited = dict()
        global hasCycle
        hasCycle = False
        def traverse(start):
            global hasCycle
            if start in path:
                hasCycle = True
                return
            if hasCycle or start in visited:
                return
            path[start] = True
            visited[start] = True
            for i in adjacent[start]:
                if i in adjacent:
                    traverse(i)
                    if i in path and not hasCycle:
                        del path[i]
            del path[start]
        for i in range(numCourses):
            if i in adjacent:
                traverse(i)
        return (not hasCycle)
            
        