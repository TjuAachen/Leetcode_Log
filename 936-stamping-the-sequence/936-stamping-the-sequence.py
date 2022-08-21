class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_freq = collections.Counter(stamp)
        target_freq = collections.Counter(target)
        
        #when target contain a char not in stamp
        for key in target_freq:
            if key not in stamp_freq:
                return []
        
        stamp_len, target_len = len(stamp), len(target)
        indegree = [stamp_len] * (target_len - stamp_len + 1)
        queue = deque()
        edge = [set() for _ in range(target_len)]
        #sliding window of fix length
        left = 0
        while(left <= target_len - stamp_len):
            right = left + stamp_len
            target_substring = target[left:right]
            for i in range(stamp_len):
                if stamp[i] == target_substring[i]:
                    indegree[left] -= 1
                else:
                   # print(left+i)
                    edge[left+i].add(left)
            if indegree[left] == 0:
                queue.append(left)
            left += 1
        
        ans = []
        while(queue):
            size = len(queue)
            for _ in range(size):
                popped = queue.popleft()
                ans.append(popped)
                for i in range(popped, popped + stamp_len):
                    for window in edge[i]:
                        indegree[window] -= 1
                        if indegree[window] == 0:
                            queue.append(window)
                    edge[i] = set()
                            
        if len(ans) == target_len - stamp_len + 1:
            return ans[::-1]
        return []
        
        
        
        
        
        
        
        