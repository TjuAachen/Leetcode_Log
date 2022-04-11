class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        global count
        count = 0
        track = []
        visited = dict()
        def permutation(n):
            global count
            if len(track) == n:
                count += 1
                if count == k:
                    return True
                return False
            for i in range(1,n+1):
                if i not in visited:
                    track.append(i)
                    visited[i] = 1
                    if permutation(n):
                        return True
                    del visited[i]
                    track.pop()
        permutation(n)
        return ''.join([str(i) for i in track])
        
            
        