class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])
    def union(self, p, q):
        parent_p, parent_q = self.find(p), self.find(q)
        self.parent[parent_q] = parent_p
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        record = {}
        def check(s1, s2):
            if len(s1) != len(s2):
                return False
            if s1 == s2:
                return True
            expected = (ord(s1[0]) - ord(s2[0]))%26
            for ind, char in enumerate(s1):
                cur = (ord(s1[ind]) - ord(s2[ind]))%26
                if cur != expected:
                    return False
            return True
        stringsNum = len(strings)
        union_set = Union(stringsNum)
        for i in range(stringsNum):
            for j in range(i+1, stringsNum):
                s1, s2 = strings[i], strings[j]
                if check(s1, s2):
                    union_set.union(i, j)
        res = {}
        for i in range(stringsNum):
            key = union_set.find(i)
            if key in res:
                res[key].append(strings[i])
            else:
                res[key] = [strings[i]]
        return list(res.values())
            